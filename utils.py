import pyautogui as pg
import sys
from time import sleep
import pygetwindow as gw


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


def move_mouse(path):
    res = pg.locateCenterOnScreen(path, confidence=0.8)
    if res != None:
        pg.moveTo(res)
        sleep(0.5)
    else:
        print('Could not find item on screen!  ' + path)
    return res


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()
    return True

def focus_window(name):
    res = gw.getWindowsWithTitle(name)[0]
    res.restore()
    res.minimize()
    res.restore()
    res.maximize()