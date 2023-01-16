from applicaitons import Applications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse
from commands import Commands


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
        sleep(0.1)
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

    def change_to_underlined(self):
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
        pg.press('e')
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

    def find_replace(self):
        pg.keyDown('ctrl')
        pg.press('h')
        pg.keyUp('ctrl')
        sleep(0.1)

    def select_all(self):
        pg.keyDown('ctrl')
        pg.press('a')
        pg.keyUp('ctrl')
        sleep(0.1)

    def tab_back(self):
        pg.keyDown('shift')
        pg.press('tab')
        pg.keyUp('shift')
        sleep(0.1)

    def find_edit_words(self, text_to_edit, command, obj):
        self.find_replace()
        # selects all and deletes, in case there are any other words in the text box
        self.select_all()
        pg.press('backspace')
        pg.write(text_to_edit)

        if pg.locateCenterOnScreen('img\\find_replace_more.png') is not None:
            print('find and replace MORE not none')
            move_and_click('img\\find_replace_more.png')
            self.tab_back()
        else:
            pg.press('tab')

        if pg.locateCenterOnScreen('img\\find_replace_no_formatting.png') is not None:
            print('find_replace_no_formatting not none')
            move_and_click('img\\find_replace_no_formatting.png')



        # pg.press('tab')
        self.select_all()
        pg.press('backspace')
        text = Commands(command)
        res = text.contains_text()
        print(res)
        sleep(1)
        text.execute(res, obj, True)

        if pg.locateCenterOnScreen('img\\find_replace_more.png') is not None:
            print('find and replace MORE not none')
            move_and_click('img\\find_replace_more.png')

        if pg.locateCenterOnScreen('img\\find_replace_whole_words.png', confidence=0.9) is not None:
            print('find replace whole words not none')
            move_and_click('img\\find_replace_whole_words.png')
        elif pg.locateCenterOnScreen('img\\find_replace_whole_words_checked.png', confidence=0.9) is not None:
            print('find_replace_whole_words_checked.png not none')

        move_mouse('img\\find_replace_actions.png')
        move_and_click('img\\find_replace_find_less.png')
        pg.press('tab', presses=2)
        pg.press('enter')
        # move_and_click('img\\find_replace_replace_all.png')

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
