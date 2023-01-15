from applicaitons import Applications
import pyautogui as pg
from time import sleep
from utils import move_and_click


class Word(Applications):
    words = []

    def create_blank_docx(self):
        res_full_screen = None
        res_small_screen = None
        res_full_screen = move_and_click('img\\new_word.png')
        if res_full_screen is None:
            res_small_screen = move_and_click('img\\new_word_smaller.png')
        res_press_blank = move_and_click('img\\word_new_blank.png')
        if res_full_screen is not None or res_small_screen is not None:
            if res_press_blank is not None:
                print('Successfully created a blank document!')
            else:
                print('Could not create a blank document! - create_blank_docx (check 1)')
        else:
            print('Could not create a blank document! - create_blank_docx (check 2)')

    def get_text(self):
        text = pg.prompt(text='', title='', default='')
        return text

    def write_text(self, text):
        pg.write(text)
        sleep(0.5)
        print('Successfully written ' + text)

    def change_to_bold(self):
        pg.keyDown('ctrl')
        pg.press('b')
        pg.keyUp('ctrl')
        sleep(0.1)

    def change_to_italic(self):
        pg.keyDown('ctrl')
        pg.press('i')
        pg.keyUp('ctrl')
        sleep(0.1)

    def change_to_underline(self):
        pg.keyDown('ctrl')
        pg.press('u')
        pg.keyUp('ctrl')
        sleep(0.1)

    def edit_text(self):
        pg.keyDown('ctrl')
        pg.press('h')
        pg.keyUp('ctrl')
        sleep(0.1)

    def align_center(self):
        pg.keyDown('ctrl')
        pg.press('h')
        pg.keyUp('ctrl')
        sleep(0.1)

    def align_left(self):
        pg.keyDown('ctrl')
        pg.press('l')
        pg.keyUp('ctrl')
        sleep(0.1)

    def align_right(self):
        pg.keyDown('ctrl')
        pg.press('r')
        pg.keyUp('ctrl')
        sleep(0.1)

    def align_justify(self):
        pg.keyDown('ctrl')
        pg.press('j')
        pg.keyUp('ctrl')
        sleep(0.1)

    def write_title(self, text):
        self.align_center()
        self.change_to_bold()
        pg.write(text)
        self.change_to_bold()
        sleep(0.1)

    def add_bullet_list(self):
        res = move_and_click('img\\word_search_bar')
        if res is not None:
            pg.write('Bullets')
            sleep(0.1)
            pg.press('enter')
            sleep(0.05)
            print('Bullet list successfully added!')
        else:
            print('Bullet list could not be created')
