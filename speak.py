import pyttsx3 as pt
import json
from random import randint


class Speak:
    def __init__(self) -> None:
        self.engine = pt.init()
        self.engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    def onEnd(name, completed):
        print('finished')

    def simple_speak(self, text):
        self.engine.connect('finished-utterance', self.onEnd)
        self.engine.say(text)
        self.engine.runAndWait()
        return True

    def speak(self, action, start):
        text = self._decode_speech_feedback(action, start)
        self.engine.say(text)
        self.engine.runAndWait()
        return True

    def _decode_speech_feedback(self, action, last_app, start):
        with open('jsons/all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            return comm[action]['start_responses'][0]
        elif start == False:
            return comm[action]['stop_responses'][0]
        elif start == None:
            print('#todo')

    def speak_system(self, action, start):
        text = self._decode_speech_feedback_system(action, start)
        self.engine.say(text)
        self.engine.runAndWait()

    def _decode_speech_feedback_system(self, action, start):
        with open('jsons/all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            return comm[action]['start_responses'][0]
        elif start == False:
            return comm[action]['stop_responses'][0]
        elif start == None:
            print('#todo')
