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
                return True
        return False

    def get_text(self, text, title):
        text = pg.prompt(text=text, title=title, default='')
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

    def go_to_beginning(self):
        pg.keyDown('ctrl')
        pg.press('home')
        pg.keyUp('ctrl')
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
        text.execute(res, obj)

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
        sleep(0.5)
        if pg.locateCenterOnScreen('img\\find_replace_confirm_research.png', confidence=0.9) is not None:
            print('found')
            pg.press('enter')
        pg.press('enter')

        if pg.locateCenterOnScreen('img\\find_replace_cancel.png') is not None:
            print('find and replace MORE not none')
            move_and_click('img\\find_replace_cancel.png')

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

    def verify_before_enter(self):
        if pg.locateCenterOnScreen('img\\find_replace_confirm_research.png', confidence=0.8) is not None:
            sleep(0.1)
            pg.press('enter')
            sleep(0.1)

    def find_edit_first(self, text_to_edit, command, obj, place):
        self.go_to_beginning()
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
        text.execute(res, obj)

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

        pg.press('tab', presses=3)
        pg.press('enter', presses=place)
        self.verify_before_enter()
        self.tab_back()
        self.tab_back()
        pg.press('enter')
        self.verify_before_enter()
        sleep(0.5)

        pg.press('enter')
        if pg.locateCenterOnScreen('img\\find_replace_cancel.png') is not None:
            print('find and replace MORE not none')
            move_and_click('img\\find_replace_cancel.png')

    def create_new_doc(self):
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
