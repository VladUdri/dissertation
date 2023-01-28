from final_applications import Applicationss
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse
from commands import Commands


class Word(Applicationss):

    def create_new_doc(self):
        self.open_app()
        print('Creating new word document...')
        pg.sleep(1)
        pg.press('enter')
        pg.sleep(1)
        print('Word document successfully created!')
        return True

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


    def word_create_new(self):
        self.open_app()
        if self.get_state() == 'open':
            pg.press('enter')
            sleep(1)
            print('New doc created.')
            return True
        elif self.get_state() == 'new_created':
            self.create_new_default()
            sleep(1)
            print('New doc created.')
            return True
        elif self.get_state() == 'closed':
            self.set_state('open')
            return self.word_create_new()
        return False