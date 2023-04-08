# from app_interface import AppInt
from voice_interpretor import VoiceInterpretor
# from voice_commands_listener import VoiceCommandListener
# from speak import Speak
from voicev import Voicev
from init_voice import VoiceInit
REC, SAMPLERATE = VoiceInit().setUp()

global last_app
last_app = ''

if __name__ == '__main__':
    
    # try:
    # todo add init speak
    # x = Voicev().listen_for_commands()
    # print(x)
    # VoiceInit().setUp()
    print(REC)
    # res = VoiceCommandListener().listen_for_commands()
    res = VoiceInterpretor()
    res.execute('open outlook')
    res.execute('create event')
    res.execute('add start time')


    # except Exception as e:
    # print('exception', e)
    # todo add error speak
    # AppInt().run()
    
