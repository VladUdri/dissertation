from init_voice import VoiceInit
REC, SAMPLERATE = VoiceInit().setUp()

from voicev import Voicev
from speak import Speak
from voice_commands_listener import VoiceCommandListener
from voice_interpretor import VoiceInterpretor



if __name__ == '__main__':
    # try:
    # todo add init speak
    # Voicev().listen_for_commands()
    # VoiceInit().setUp()
    # print(REC)
    # res = VoiceCommandListener().listen_for_commands()
    res = VoiceInterpretor()
    res.execute('open microsoft word')

    # except Exception as e:
    # print('exception', e)
    # todo add error speak
