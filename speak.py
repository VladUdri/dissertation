import pyttsx3 as pt
import json
from random import randint


class Speak:
    def __init__(self) -> None:
        self.engine = pt.init()
        self.engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    def onEnd(name, completed):
        print ('finished')

    def simple_speak(self, text):
        self.engine.connect('finished-utterance', self.onEnd)
        self.engine.say(text)
        self.engine.runAndWait()
        return True


    def speak(self, action, app, start):
        text = self.__decode_speech_feedback(action, app._app_name, start)
        self.engine.say(text)
        self.engine.runAndWait()
        return True

    def __decode_speech_feedback(self, action, last_app, start):
        with open('all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            index = randint(
                0, len(comm['default_commands'][action]['start_responses']) - 1)
            return comm['default_commands'][action]['start_responses'][index].replace('<app_name>', last_app)
        elif start == False:
            index = randint(
                0, len(comm['default_commands'][action]['stop_responses']) - 1)
            return comm['default_commands'][action]['stop_responses'][index].replace('<app_name>', last_app)
        elif start == None:
            print('#todo')

    def speak_system(self, action, start):
        text = self.__decode_speech_feedback_system(action, start)
        self.engine.say(text)
        self.engine.runAndWait()

    def __decode_speech_feedback_system(self, action, start):
        with open('all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            index = randint(
                0, len(comm['default_commands'][action]['start_responses']) - 1)
            return comm['default_commands'][action]['start_responses'][index]
        elif start == False:
            index = randint(
                0, len(comm['default_commands'][action]['stop_responses']) - 1)
            return comm['default_commands'][action]['stop_responses'][index]
        elif start == None:
            print('#todo')
