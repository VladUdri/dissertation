from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window
import time
from voicev import Voicev


class Notepad(IApplications):
    def __init__(self, _app_name='notepad', state='closed'):
        super().__init__(_app_name, state)

    def create_new(self):
        focus_window(self._app_name)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    def save_as(self):
        self.key_action.execute(['press', 'alt', 'press', 'f',
                                 'press', 'a'])
        self._save_replace()

    def _save_replace(self):
        self.speak.simple_speak('What should be the name of the note?')
        name = Voicev().listen_for_commands(True)
        pg.write(name)
        sleep(1)
        self.key_action.execute(['press', 'enter'])
        sleep(1)
        if pg.locateOnScreen('images\warning.png') is not None:
            self.speak.simple_speak(
                'This already exists! Do you want to replace it?')
            response = Voicev().listen_for_commands(True)
            if response == 'yes':
                self.key_action.execute(['press', 'left', 'press', 'enter'])
            elif response == 'no':
                self.key_action.execute(['press', 'right', 'press', 'enter'])
                self._save_replace()

    def create_new_edited(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

                                 
        # #########################################################################################
