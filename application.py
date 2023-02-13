import pyautogui as pg
from time import sleep
from AppOpener import open
import psutil
import pygetwindow as gw
from abc import ABC, abstractmethod
from images.vosk_voice import VoskModel
from speak import Speak
from key_action import KeyAction
'''
State rules: 
    ### 'close' = app is not opened;
    ### 'open' = app just got open, default open settings;
    ### 'new_created' = app has a new document/email created;
'''


class IApplications(ABC):
    def __init__(self, app_name, state='closed'):
        self._app_name = app_name
        self._state = state
        self.listen = VoskModel()
        self.speak = Speak()
        self.key_action = KeyAction()

    @abstractmethod
    def create_new(self):
        pass

    # to use
    def is_app_open(self):
        for p in psutil.process_iter():
            if self._app_name.lower() in p.name().lower():
                return True
        return False

    '''
    In order to open an application, we use the method open from the AppOpener library.
    '''
    # to use

    def open_app(self):
        open(self._app_name)
        self._state = 'open'
        sleep(2)
        return True

    '''
    save_as function that presses combinations of key so that it saves the document.
    It uses pyautogui to execute the presses
    '''
    # to use
    # todo add states
    # to use

    def close_app(self):
        if self.is_app_open():
            res = gw.getWindowsWithTitle(self._app_name)[0]
            res.close()
            self._state = 'closed'
            print('App closed')
            return True
        else:
            print('App is not opened!')
            return False
