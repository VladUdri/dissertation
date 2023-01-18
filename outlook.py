from applicaitons import Applications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse
from commands import Commands


class Outlook(Applications):

    def create_new(self):
        pg.keyDown('ctrl')
        pg.press('n')
        pg.keyUp('ctrl')
        sleep(0.1)

    def send(self):
        pg.keyDown('alt')
        pg.press('s')
        pg.keyUp('alt')
        sleep(0.1)

    def open_taskbar(self):
        if pg.locateCenterOnScreen('img\\taskbar_outlook.png', confidence=0.8):
            move_and_click('img\\taskbar_outlook.png')
            sleep(1)
            print('check 1')
        elif pg.locateCenterOnScreen('img\\taskbar_outlook_empty.png', confidence=0.8):
            move_and_click('img\\taskbar_outlook_empty.png')
            sleep(1)
            print('check 2')

    def send_email(self):
        self.create_new()
        sleep(1)
        to = pg.prompt('to')
        pg.write(to)
        sleep(1)
        pg.press('tab')
        sleep(0.5)
        pg.press('tab')
        cc = pg.prompt('cc')
        pg.write(cc)
        sleep(0.5)
        pg.press('tab')
        subject = pg.prompt('subject')
        pg.write(subject)
        sleep(0.5)
        pg.press('tab')
        body = pg.prompt('body')

        pg.write(body)
        sleep(1)
        self.send()
        # pg.press('tab')
