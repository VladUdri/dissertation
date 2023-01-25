from app_settings import AppSettings
import pyautogui as pg
from time import sleep
from AppOpener import open

from utils import move_and_click


class Applications(AppSettings):
    word_dict = {'word', 'ms word', 'microsoft word'}
    excel_dict = {'excel', 'ms excel', 'microsoft excel', 'spreadsheet'}
    ppt_dict = {'power point', 'powerpoint', 'microsoft power point', 'ms power point'}

    start_img = 'img/start.png'

    def __init__(self, app_name):
        super().__init__(app_name)
        self.app_name = app_name

    def get_app(self, app_name):
        if app_name in self.word_dict:
            return 'Word'
        elif app_name in self.excel_dict:
            return 'Excel'
        elif app_name in self.ppt_dict:
            return 'PowerPoint'
        elif app_name == 'Outlook':
            return 'Outlook'

    # function that presses on the start button
    def open_app(self):
        try:
            res = pg.locateCenterOnScreen('start.png', confidence=0.8)
            if res is not None:
                move_and_click('start.png')
            else:
                pg.hotkey('winleft')
            sleep(0.7)
            # gets the app name through the get_app filter
            app = self.get_app(self.app_name)
            # writes the name of the app in the search bar
            pg.write(app)
            sleep(0.5)
            self.open_btn_press(app)
        except:
            print('exception')

    # function that opens applications
    # todo make it be universal, so that it can be used by any other app (now it can only be used by word apps)
    def open_btn_press(self, app):
        try:
            res = move_and_click('img\\start_open_btn.png')
            if res is None:
                pg.hotkey('enter')
        except:
            print('exception')

    # function that saves the progress from an app (only works with Word, Ppt and Excel)
    # TODO make it work with other apps too
    def save(self, save_name):
        res = move_and_click('img\\save_icon.png')
        sleep(0.5)
        if res is not None:
            pg.write(save_name)
            sleep(0.5)
            move_and_click('img\\save.png')
            sleep(0.5)
            if pg.locateCenterOnScreen('img\\replace_file.png', confidence=0.8) is not None:
                while pg.locateCenterOnScreen('img\\replace_file.png', confidence=0.8) is not None:
                    replace = pg.prompt(text='Already exists. Replace?', title='Name for document', default='')
                    if replace == 'yes':
                        self.save_already_exists('replace', '')
                    else:
                        new_name = pg.prompt(text='New name', title='Name for document', default='')
                        self.save_already_exists('change name', new_name)
            else:
                print('Successfully saved!')
                return True
        else:
            pg.hotkey('ctrl', 's')
        return True

    def save_already_exists(self, action, new_name):
        print('This name already exists.')
        if action == 'replace':
            replace_result = move_and_click('img\\replace_file.png')
            if replace_result is not None:
                replace_result_ok = move_and_click('img\\ok.png')
                if replace_result_ok is not None:
                    print('Successfully saved!')
                    return True
                else:
                    print('Could not save!')
                    return False
            else:
                print('Could not save!')
                return False

        elif action == 'change name':
            if pg.locateCenterOnScreen('img\\save_different_name.png') is not None:
                while move_and_click('img\\save_different_name.png') is not None:
                    replace_result_ok = move_and_click('img\\ok.png')
                    if replace_result_ok is not None:
                        # TODO add that the program asks for a name here
                        pg.write(new_name)
                        sleep(0.5)
                        move_and_click('img\\save.png')
                        sleep(0.5)
                print('Successfully saved!')
            else:
                print('Could not save!')

    '''
    In order to open an application, we use the method open from the AppOpener library.
    '''

    def open_application(self):
        open(self.app_name)
        sleep(3)
        return True

    def close_application(self):
        pg.keyDown('alt')
        pg.press('f4')
        pg.keyUp('alt')

    '''
    save_as function that presses combinations of key so that it saves the document.
    It uses pyautogui to execute the presses
    '''

    def save_as(self):
        pg.press('alt')
        sleep(0.5)
        pg.press('f')
        sleep(0.5)
        pg.press('a')
        sleep(0.5)
        pg.press('o')
        sleep(0.5)
        name = pg.prompt('Name of document')
        pg.write(name)
        sleep(1)
        pg.press('enter')
