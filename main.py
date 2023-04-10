# from app_interface import AppInt
from voice_interpretor import VoiceInterpretor
# from voice_commands_listener import VoiceCommandListener
# from speak import Speak
from time import sleep
from voicev import Voicev
from init_voice import VoiceInit
REC, SAMPLERATE = VoiceInit().setUp()

global last_app
last_app = 'google'

if __name__ == '__main__':
    
    # try:
    # todo add init speak
    # x = Voicev().listen_for_commands()
    # print(x)
    # VoiceInit().setUp()
    # print(REC)
    # res = VoiceCommandListener().listen_for_commands()
    res = VoiceInterpretor()
    # res.execute('open outlook')
    # res.execute('compose email outlook')
    # sleep(5)
    # res.execute('add end time')
    # print('SUNT IN add subject')

    # res.execute('add subject')
    # print('SUNT IN add recipient')

    # res.execute('add recipient')
    # print('SUNT IN add cc')

    res.execute('computer decrease brightness')
    res.execute('decrease brightness')
    res.execute('decrease brightness')
    res.execute('decrease brightness')
    res.execute('decrease brightness')

    # print('SUNT IN write email')

    # res.execute('write email')

    # except Exception as e:
    # print('exception', e)
    # todo add error speak
    # AppInt().run()
    
