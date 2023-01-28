import pyautogui as pg
import keyboard as kb
import time

class AppSettings:
    def __init__(self, app_name, state):
        self._app_name = app_name
        self._state = state
