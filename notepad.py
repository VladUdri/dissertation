from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window
import time


class Notepad(IApplications):
    def __init__(self, app_name, state):
        super().__init__(app_name, state)

# #########################################################################################
    def create_new(self):
        focus_window(self._app_name)
        if self._state == 'open':
            return True
        elif self._state == 'edited':
            self.create_new_edited()
            sleep(1)
            print('New doc created.')
            return True
        return False

    def save_as(self):
        self.key_action.execute(['press', 'alt', 'press', 'f',
                                 'press', 's'])
        self.__save_replace()

    def create_new_edited(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])
        # #########################################################################################
