from final_applications import Applicationss
import pyautogui as pg
from time import sleep
from utils import focus_window
from commands import Commands


class Outlook(Applicationss):

    def create_new(self):
        focus_window(self._app_name)
        sleep(0.5)
        pg.keyDown('ctrl')
        pg.press('n')
        pg.keyUp('ctrl')
        sleep(0.1)

    def send(self):
        pg.keyDown('alt')
        pg.press('s')
        pg.keyUp('alt')
        sleep(0.1)

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
