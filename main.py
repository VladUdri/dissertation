# from app_interface import AppInt
import json
from voice_interpretor import VoiceInterpretor
from voice_commands_listener import VoiceCommandListener
# from speak import Speak
from time import sleep
from voicev import Voicev
from init_voice import VoiceInit
REC, SAMPLERATE = VoiceInit().setUp()


if __name__ == '__main__':
    with open('jsons/all_commands.json') as f:
        comm = json.load(f)
    #     # try:
    #     # todo add init speak

    #     # VoiceInit().setUp()
    #     # print(REC)
    # res = VoiceCommandListener().listen_for_commands()

    res = VoiceInterpretor(comm)
#     #     res.execute('open outlook')
#     #     res.execute('create new email')
#     #     res.execute('compose email outlook')
#     #     # sleep(5)
#     #     # res.execute('add end time')
#     #     # print('SUNT IN add subject')

    # res.execute('open word')
    # res.execute('create new blank')
    # sleep(5)
    res.execute('sleep well')
    # res.execute('select all')

#     with open('jsons/last_app/last_app.txt', 'w') as h:
#         h.write('')
#     #     # sleep(3)
#     #     # res.execute('start dictating')
#     #     # res.execute('save notepad')
