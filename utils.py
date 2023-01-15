from app_settings import AppSettings
import pyautogui as pg
import sys
from time import sleep
import os

def move_and_click(path):
    res = pg.locateCenterOnScreen(path, confidence=0.8)
    if res != None:
        pg.moveTo(res)
        sleep(0.5)
        pg.click()
        sleep(0.5)
    else:
        print('Could not find item on screen!  ' + path)
    return res