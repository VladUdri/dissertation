from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window
from voicev import Voicev
from word2number import w2n


class Word(IApplications):
    def __init__(self, app_name='word', state='closed'):
        super().__init__(app_name, state)

# #########################################################################################
    def create_new(self):
        focus_window(self._app_name)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    def word_create_new_blank(self):
        focus_window(self._app_name)
        self.key_action.execute(['press', 'alt', 'press', 'n',
                                 'press', 'l'])
        sleep(2)

    def save_as(self):
        focus_window(self._app_name)
        self.key_action.execute(['press', 'alt', 'press', 'f',
                                 'press', 'a', 'press', 'o'])
        self.__save_replace()

    def __save_replace(self):
        self.speak.simple_speak('What should be the name of the document?')
        name = Voicev().listen_for_commands(True)

        pg.write(name)
        sleep(1)
        self.key_action.execute(['press', 'enter'])
        sleep(1)
        if pg.locateOnScreen('images\save_replace.png', grayscale=True) is not None:
            self.speak.simple_speak(
                'This already exists! Do you want to replace it?')
            response = Voicev().listen_for_commands(True)

            if response == 'yes':
                self.key_action.execute(['press', 'enter'])
            elif response == 'no':
                self.key_action.execute(['press', 'down', 'press', 'enter'])
                self.__save_replace()

    '''
    Function that changes the font of the writing.
    It uses pyautoguy to execute word keyboard shortcuts
    '''

    def word_change_font(self):
        focus_window(self._app_name)
        print('Changing font...')
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(1)
        font = Voicev().listen_for_commands(True)
        sleep(0.5)
        pg.write(font)
        sleep(0.5)
        pg.press('enter')

        '''
        Function that changes the font size of the writing.
        It uses pyautoguy to execute word keyboard shortcuts
        '''

    def word_change_size(self):
        focus_window(self._app_name)
        print('Changing font...')
        sleep(1)
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(0.5)
        self.key_action.execute(
            ['key_down', 'alt', 'press', 's', 'key_up', 'alt'])
        int_size = None
        while int_size is None:
            try:
                size = Voicev().listen_for_commands(True)
                print(size)
                int_size = w2n.word_to_num(size)
                print(str(int_size))
                sleep(0.5)
            except:
                print('repeta')
                int_size = None
        pg.write(str(int_size))
        sleep(0.5)
        pg.press('enter')

# #########################################################################################
