import pyautogui as pg
from time import sleep
from AppOpener import open
import psutil
from app_settings import AppSettings
from utils import move_and_click
import pygetwindow as gw

'''
State rules: 
    ### 'close' = app is not opened;
    ### 'open' = app just got open, default open settings;
    ### 'new_created' = app has a new document/email created;
'''


class Applicationss(AppSettings):
    def __init__(self, app_name, state):
        self._app_name = app_name
        self._state = state

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
        self.set_state('open')
        sleep(3)
        return True

    # to delete
    def close_command(self):
        pg.keyDown('alt')
        pg.press('f4')
        pg.keyUp('alt')
        return True

    '''
    save_as function that presses combinations of key so that it saves the document.
    It uses pyautogui to execute the presses
    '''
    # to use

    def save_as(self, get_name):
        pg.press('alt')
        sleep(0.5)
        pg.press('f')
        sleep(0.5)
        pg.press('a')
        sleep(0.5)
        pg.press('o')
        sleep(0.5)
        name = get_name
        pg.write(name)
        sleep(1)
        pg.press('enter')

    # todo add states
    # to use
    def close_app(self):
        if self.is_app_open():
            res = gw.getWindowsWithTitle(self._app_name)[0]
            res.close()
            self.set_state('closed')
            print('App closed')
            return True
        else:
            print('App is not opened!')
            return False

    def create_new_default(self):
        pg.keyDown('ctrl')
        pg.press('n')
        pg.keyUp('ctrl')
        sleep(1)
        return True

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state
