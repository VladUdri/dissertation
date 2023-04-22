import json
from speak import Speak
from speech_commands_listener import SpeechCommandListener
from speak import Speak
from init_voice import VoiceInit
import pyautogui as pg
REC, SAMPLERATE = VoiceInit().setUp()


if __name__ == '__main__':

    try:
        # Call the listen_for_commands function from SpeechCommandListener.py
        # to start the speech recognition system
        SpeechCommandListener().listen_for_commands(REC, SAMPLERATE)
    except:
        # If an exception occurs, provide speech feedback about it
        speaker = Speak()
        speaker.simple_speak('Something went wrong? please try again!')
        with open('jsons/last_app/last_app.txt', 'w') as h:
            h.write('')
    else:
        # If everything works well, delete the contents of the last_app.txt
        # file so it can be reused when the program starts again

        with open('jsons/last_app/last_app.txt', 'w') as h:
            h.write('')
