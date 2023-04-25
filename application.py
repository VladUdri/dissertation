from time import sleep
from AppOpener import open
import psutil
import pygetwindow as gw
from abc import ABC
from speak import Speak
from key_action import KeyAction
from utils import focus_window


class IApplications(ABC):
    def __init__(self, app_name):
        self._app_name = app_name
        self.speak = Speak()
        self.key_action = KeyAction()

    '''
    In order to open an application, we use the method open from the AppOpener library.
    '''
    # Funtion that opens an app. If app cannot be found, give speech feedback
    def open_app(self):
        try:
            open(self._app_name)
            sleep(3)
            focus_window(self._app_name)

            return True
        except:
            self.speak.simple_speak('I don\'t know this app!')
            return

    # Function that checks if an app is open or not
    def is_app_open(self):
        for p in psutil.process_iter():
            if self._app_name.lower() in p.name().lower():
                return True
        return False

    # Funtion that closes an app. If app is not opened, give speech feedback

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
