import pyautogui as pg
from time import sleep
from AppOpener import open
import psutil
import pygetwindow as gw
from abc import ABC
from speak import Speak
from key_action import KeyAction
'''
State rules: 
    ### 'close' = app is not opened;
    ### 'open' = app just got open, default open settings;
    ### 'new_created' = app has a new document/email created;
'''


class IApplications(ABC):
    def __init__(self, app_name):
        self._app_name = app_name
        self.speak = Speak()
        self.key_action = KeyAction()

    '''
    In order to open an application, we use the method open from the AppOpener library.
    '''
    # to use

    def open_app(self):
        try:
            open(self._app_name)
            sleep(2)
            return True
        except:
            self.speak.simple_speak('I don\'t know this app!')
            return

    def is_app_open(self):
        for p in psutil.process_iter():
            if self._app_name.lower() in p.name().lower():
                return True
        return False

    '''
    save_as function that presses combinations of key so that it saves the document.
    It uses pyautogui to execute the presses
    '''

    def close_app(self):
        if self.is_app_open():
            res = gw.getWindowsWithTitle(self._app_name)[0]
            res.close()
            self.key_action.execute(
                ['key_down', 'alt', 'press', 'n', 'key_up', 'alt'])
            self.speak.simple_speak('Done closing!')

            return True
        else:
            self.speak.simple_speak('App is not opened!')
            return False
