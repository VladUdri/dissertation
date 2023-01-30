from final_word import Word
import json
import execution
import pyttsx3 as pt
import pyautogui as pg
import pygetwindow as gw
from time import sleep

if __name__ == '__main__':
    last_app = ''
    engine = pt.init()
    engine.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    last_app = execution.execute('please open outlook', engine, last_app)
    sleep(1)
    last_app = execution.execute('compose new outlook', engine, last_app)
    # execution.decode_speech_feedback('open_app', 'word')
    # print('####'*10)
    # print(last_app)
