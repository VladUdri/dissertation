from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window
import time
from voicev import Voicev
import webbrowser


class Google(IApplications):
    def __init__(self, app_name='google', state='closed'):
        super().__init__(app_name, state)

    def create_new(self):
        pass

    def google_search(self):
        print('here')
        url = 'https://www.google.com/search?q='
        self.speak.simple_speak(
            'What do you want to search?')
        res = Voicev().listen_for_commands(True)
        url += res
        webbrowser.get().open(url)
    
    def google_wikipedia_search(self):
        url = 'https://en.wikipedia.org/wiki/'
        self.speak.simple_speak(
            'What do you want to search on Wikipedia?')
        res = Voicev().listen_for_commands(True)
        url += res
        webbrowser.get().open(url)

