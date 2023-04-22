from convert_text import ConvertText
import json
from time import sleep
from speak import Speak
from command_interpretor import CommandInterpretor
default_apps = {'word': ['word', 'microsoft word'], 'outlook': ['outlook', 'microsoft outlook'], 'computer': [
    'computer'], 'notepad': ['notepad', 'microsoft notepad', 'note'], 'google': ['google', 'wikipedia']}


class VoiceInterpretor:
    def __init__(self, comm) -> None:
        self.comm = comm
        with open('jsons/custom_commands.json') as g:
            self.custom_comm = json.load(g)
        with open('jsons/last_app/last_app.txt') as h:
            self.last_app = h.readlines()
        self.speaker = Speak()

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

    def _search_str(self, text, app):
        for key in self.comm:
            for i in range(0, len(self.comm[key]['patterns'])):
                if all(substring in text.lower() for substring in self.comm[key]['patterns'][i]):
                    if app in self.comm[key]['apps'] or not self.comm[key]['apps']:
                        return key
        return None

    def _search_custom(self, text):
        for key in self.custom_comm:
            if key == text:
                return key
        return None

    def execute(self, phrase):
        convertion = ConvertText(phrase)
        converted_text = convertion.process_text()
        print(converted_text)
        text_to_compare = ' '.join(converted_text[0:len(converted_text)])
        app = self._get_app(text_to_compare)
        if app is None:
            app = 'computer'
        custom = ''
        action = self._search_str(text_to_compare, app)
        if action is None:
            custom = self._search_custom(phrase)
            if custom is not None:
                app = action = 'custom'
            else:
                self.speaker.simple_speak(
                    'Sorry! I don\'t know that.')

                return None
        CommandInterpretor(app, self.last_app, custom).process_command(action)
        return None
