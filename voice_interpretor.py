from time import sleep
from convert_text import ConvertText
import json
from utils import speak
from random import randint
from command_interpretor import CommandInterpretor

default_apps = ['word', 'outlook', 'computer', 'notepad', 'google']

start_apps = {}


class VoiceInterpretor():
    def __init__(self) -> None:
        with open('all_commands.json') as f:
            self.comm = json.load(f)

    def get_app(self, text):
        for word in text.split(' '):
            if word in default_apps:
                return word
        return None

    def search_str(self, text):
        for key in self.comm['default_commands']:
            for i in range(0, len(self.comm['default_commands'][key]['patterns'])):
                if all(substring in text.lower() for substring in self.comm['default_commands'][key]['patterns'][i]):
                    return key
        return None

    def execute_app(self, app, action, engine):
        if action not in default_apps[app]:
            return False
        self.default_actions(start_apps[app], action, app, engine)

    def execute(self, phrase):
        convertion = ConvertText(phrase)
        converted_text = convertion.process_text()
        print(converted_text)
        text_to_compare = ' '.join(converted_text[0:len(converted_text)])
        print(text_to_compare)

        action = self.search_str(text_to_compare)
        print(action)
        if action is not None:
            app = self.get_app(text_to_compare)
            print(app)
            if app is not None:
                last_app = app
            else:
                if last_app != '':
                    app = last_app
                else:
                    # todo maybe something else
                    # speak(engine=engine,
                    #       text='Please say the command again, but specify the app!')
                    return
        else:
            # speak(engine=engine, text='Sorry! I don\'t know that.')
            return
        CommandInterpretor().process_command(action)
        # self.startup_app(app)
        # res = self.execute_app(app=app, action=action, engine=engine)
        # if res == False:
        #     speak('Action not available for this app.')
        #     return
        # return last_app
        # todo add command interpretor
