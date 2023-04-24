# import necessary modules
from convert_text import ConvertText
import json
from speak import Speak
from command_interpreter import CommandInterpreter

# define default apps and their aliases
default_apps = {'word': ['word', 'microsoft word'], 'outlook': ['outlook', 'microsoft outlook'], 'computer': [
    'computer'], 'notepad': ['notepad', 'microsoft notepad', 'note'], 'google': ['google', 'wikipedia']}

# define the VoiceInterpreter class
class VoiceInterpreter:
    # initialize the class
    def __init__(self) -> None:
        # load commands from JSON files
        with open('jsons/all_commands.json') as f:
            self.comm = json.load(f)
        with open('jsons/custom_commands.json') as g:
            self.custom_comm = json.load(g)
        with open('jsons/last_app/last_app.txt') as h:
            self.last_app = h.readlines()
        # create a Speak object to speak responses
        self.speaker = Speak()

    # get the current application based on the text input
    def _get_app(self, text):
        try:
            for word in text.split(' '):
                for key, app in default_apps.items():
                    if word in app:
                        self.last_app = key
                        with open('jsons/last_app/last_app.txt', 'w') as h:
                            h.write(self.last_app)
                        return key
            if isinstance(self.last_app, list):
                return self.last_app[0]
            return self.last_app
        except:
            return None

    # search for a matching command in the predefined commands
    def _search_str(self, text, app):
        for key in self.comm:
            for i in range(0, len(self.comm[key]['patterns'])):
                if all(substring in text.lower() for substring in self.comm[key]['patterns'][i]):
                    if app in self.comm[key]['apps'] or not self.comm[key]['apps']:
                        return key
        return None

    # search for a matching custom command
    def _search_custom(self, text):
        for key in self.custom_comm:
            if key == text:
                return key
        return None

    # execute the given voice command
    def execute(self, phrase):
        # convert the voice input to text and get the current app
        convertion = ConvertText(phrase)
        converted_text = convertion.process_text()
        text_to_compare = ' '.join(converted_text[0:len(converted_text)])
        app = self._get_app(text_to_compare)
        if app is None:
            app = 'computer'
        custom = ''
        # search for a matching predefined command
        action = self._search_str(text_to_compare, app)
        if action is None:
            # if no predefined command is found, search for a matching custom command
            custom = self._search_custom(phrase)
            if custom is not None:
                app = action = 'custom'
            else:
                # if no matching command is found, speak a response and return None
                self.speaker.simple_speak(
                    'Sorry! I don\'t know that.')
                return None
        # if a matching command is found, process it using the CommandInterpreter class and return None
        CommandInterpreter(app, self.last_app, custom).process_command(action)
        return None
