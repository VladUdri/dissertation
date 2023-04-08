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
        with open('jsons/all_commands.json') as f:
            self.comm = json.load(f)
        with open('jsons/custom_commands.json') as g:
            self.custom_comm = json.load(g)

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

    def search_custom(self, text):
        for key in self.custom_comm:
            if key == text:
                return key
        return None

    def execute(self, phrase):
        convertion = ConvertText(phrase)
        converted_text = convertion.process_text()
        # print(converted_text)
        text_to_compare = ' '.join(converted_text[0:len(converted_text)])
        print('Voice_interpretor: text_to_compare = ', text_to_compare)

        action = self.search_str(text_to_compare)
        custom = ''
        # print('Voice_interpretor: action = ', action, '\n')
        if action is not None:
            app = self.get_app(text_to_compare)
            # print('Voice_interpretor: app = ', app, '\n')
        else:
            # speak(engine=engine, text='Sorry! I don\'t know that.')
            custom = self.search_custom(phrase)
            if custom is not None:
                app = action = 'custom'
            else:
                return
        CommandInterpretor(app, custom).process_command(action)
        # self.startup_app(app)
        # res = self.execute_app(app=app, action=action, engine=engine)
        # if res == False:
        #     speak('Action not available for this app.')
        #     return
        # return last_app
        # todo add command interpretor
