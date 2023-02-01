from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window


class Word(IApplications):
    def __init__(self, app_name, state):
        super().__init__(app_name, state)

    def create_new(self):
        focus_window(self._app_name)
        if self._state == 'open':
            pg.press('enter')
            sleep(1)
            print('New doc created.')
            self._state = 'new_created'
            return True
        elif self._state == 'new_created':
            self.create_new_default()
            sleep(1)
            print('New doc created.')
            return True
        return False

    def save_as(self):
        print('sunt aici ba boule')
        pg.press('alt')
        sleep(0.5)
        pg.press('f')
        sleep(0.5)
        pg.press('a')
        sleep(0.5)
        pg.press('o')
        sleep(0.5)
        name = 'lotus'
        pg.write(name)
        sleep(1)
        pg.press('enter')

    def open_font_dialog(self):
        pg.keyDown('ctrl')
        pg.press('d')
        pg.keyUp('ctrl')
        sleep(0.5)

    '''
    Function that changes the font of the writing.
    It uses pyautoguy to execute word keyboard shortcuts
    '''

    def change_font(self):
        print('Changing font...')
        sleep(1)
        self.open_font_dialog()
        font = pg.prompt(title='font')
        sleep(0.5)
        pg.write(font)
        sleep(0.5)
        pg.press('down')
        sleep(0.5)
        pg.press('enter')

    '''
        Function that changes the font size of the writing.
        It uses pyautoguy to execute word keyboard shortcuts
        '''

    def change_font_size(self):
        print('Changing font...')
        sleep(1)
        self.open_font_dialog()
        pg.press('tab', presses=2)
        size = pg.prompt(title='Font size', text='Numbers only')
        sleep(0.5)
        pg.write(size)
        sleep(0.5)
        pg.press('enter')
