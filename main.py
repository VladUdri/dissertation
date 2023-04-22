import json
from speak import Speak
from voice_interpretor import VoiceInterpretor
from speech_commands_listener import VoiceCommandListener
from speak import Speak
from voicev import Voicev
from init_voice import VoiceInit
import pyautogui as pg
REC, SAMPLERATE = VoiceInit().setUp()
with open('jsons/all_commands.json') as f:
    comm = json.load(f)

if __name__ == '__main__':

    ########################## - final - #####################################

    try:
        VoiceCommandListener(comm).listen_for_commands(REC, SAMPLERATE)
        # res = VoiceInterpretor(comm)
        # res.execute('search on google')
    except:
        speaker = Speak()
        speaker.simple_speak('Something went wrong? please try again!')
        with open('jsons/last_app/last_app.txt', 'w') as h:
            h.write('')
    else:
        with open('jsons/last_app/last_app.txt', 'w') as h:
            h.write('')

    ##########################################################################
    # res = VoiceInterpretor(comm)
    # res.execute('new command')