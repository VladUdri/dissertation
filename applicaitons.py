from app_settings import AppSettings
import pyautogui as pg
from time import sleep

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

    # function that presses on the start button
    def open_app(self):
        try:
            res = pg.locateCenterOnScreen('start.png', confidence=0.9)
            if res is not None:
                print(res)
                pg.moveTo(res)
                pg.click()
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
    def save(self, save_name, action, new_name):
        try:
            res = move_and_click('img\\save_icon.png')
            sleep(0.5)
            if res is not None:
                pg.write(save_name)
                sleep(0.5)
                move_and_click('img\\save.png')
                sleep(0.5)
                if pg.locateCenterOnScreen('img\\replace_file.png', confidence=0.8) is not None:
                    while pg.locateCenterOnScreen('img\\replace_file.png', confidence=0.8) is not None:
                        self.save_already_exists(action, new_name)
                else:
                    print('Successfully saved!')
            else:
                pg.hotkey('ctrl', 's')

        except:
            print('exception')

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
