from application import IApplications
import pyautogui as pg
from time import sleep
from utils import move_and_click, move_mouse, focus_window
from voicev import Voicev
from word2number import w2n
from speak import Speak


class Word(IApplications):
    def __init__(self, app_name='word'):
        super().__init__(app_name)

# #########################################################################################
    def word_create_new(self):
        focus_window(self._app_name)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    def word_create_new_blank(self):
        focus_window(self._app_name)
        self.key_action.execute(['press', 'alt', 'press', 'n',
                                 'press', 'l'])
        sleep(2)

    def word_save_as(self):
        focus_window(self._app_name)
        self.key_action.execute(['press', 'alt', 'press', 'f',
                                 'press', 'a', 'press', 'o'])
        sleep(1)
        self._save_replace()

    def _save_replace(self):
        name = Voicev('What should be the name of the document?').listen_for_commands(True)

        pg.write(name)
        sleep(1)
        self.key_action.execute(['press', 'enter'])
        sleep(1)
        if pg.locateOnScreen('images\save_replace.png', grayscale=True, confidence=0.8) is not None:
            self.speak.simple_speak(
                'This already exists! Do you want to replace it?')
            response = Voicev().listen_for_commands(True)

            if response == 'yes':
                self.key_action.execute(['press', 'enter'])
            elif response == 'no':
                self.key_action.execute(['press', 'down', 'press', 'enter'])
                self._save_replace()

    '''
    Function that changes the font of the writing.
    It uses pyautoguy to execute word keyboard shortcuts
    '''

    def word_change_font(self):
        focus_window(self._app_name)
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(1)
        font = Voicev('What should be the new font?').listen_for_commands(True)
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
        sleep(1)
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(0.5)
        self.key_action.execute(
            ['key_down', 'alt', 'press', 's', 'key_up', 'alt'])
        int_size = None
        while int_size is None:
            try:
                size = Voicev(
                    'What should be the new size?').listen_for_commands(True)
                int_size = w2n.word_to_num(size)
                sleep(0.5)
            except:
                Speak().simple_speak('Please say the size again!')
                int_size = None
        pg.write(str(int_size))
        sleep(0.5)
        pg.press('enter')

# #########################################################################################
