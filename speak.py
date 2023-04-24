import pyttsx3 as pt
import json
from random import randint

class Speak:
    def __init__(self) -> None:
        # Initialize the pyttsx3 engine and set the voice property
        self.engine = pt.init()
        self.engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    
    def onEnd(name, completed):
        # Print a message to indicate that the utterance has finished
        print('finished')
        
    def simple_speak(self, text):
        # Connect the engine to the "finished-utterance" event and speak the given text
        self.engine.connect('finished-utterance', self.onEnd)
        self.engine.say(text)
        self.engine.runAndWait()
        # Return True to indicate that the speaking process was successful
        return True

    def speak(self, action, start):
        # Decode the speech feedback based on the given action and start parameter
        text = self._decode_speech_feedback(action, start)
        # Speak the decoded text using the engine
        self.engine.say(text)
        self.engine.runAndWait()
        # Return True to indicate that the speaking process was successful
        return True

    def _decode_speech_feedback(self, action, start):
        # Load the commands from the "all_commands.json" file
        with open('jsons/all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            # If start is True, return the first start response for the given action
            return comm[action]['start_responses'][0]
        elif start == False:
            # If start is False, return the first stop response for the given action
            return comm[action]['stop_responses'][0]

    def speak_system(self, action, start):
        # Decode the speech feedback for the system based on the given action and start parameter
        text = self._decode_speech_feedback_system(action, start)
        # Speak the decoded text using the engine
        self.engine.say(text)
        self.engine.runAndWait()

    def _decode_speech_feedback_system(self, action, start):
        # Load the commands from the "all_commands.json" file
        with open('jsons/all_commands.json') as f:
            comm = json.load(f)
        if start == True:
            # If start is True, return the first start response for the given action
            return comm[action]['start_responses'][0]
        elif start == False:
            # If start is False, return the first stop response for the given action
            return comm[action]['stop_responses'][0]
