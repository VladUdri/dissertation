from application import IApplications
import pyautogui as pg
from time import sleep
from utils import focus_window
from vost_text import VoskModell
from commands.vosk_dictation import VoskDictation


class Outlook(IApplications):
    def __init__(self, app_name='outlook', state='closed'):
        super().__init__(app_name, state)

    def create_new(self):
        focus_window(self._app_name)
        sleep(0.5)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])
        sleep(0.1)

    def send(self):
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                 'key_up', 'alt'])
        sleep(0.1)

    def send_email(self):
        self.create_new()
        sleep(1)
        self.speak.simple_speak(
            'Who do you want to send the email to?')
        to = VoskModell().listen_for_commands(True)
        pg.write(to)
        sleep(1)
        pg.press('tab')
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'Who shoud be as cc\'s')
        cc = VoskModell().listen_for_commands(True)
        if cc != 'none' and cc != 'nobody':
            pg.write(cc)
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'What should be the subject?')
        subject = VoskModell().listen_for_commands(True)
        pg.write(subject)
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'Please start dictating. When you are done, just say stop dictating!')
        VoskDictation().execute()
        sleep(1)
        # self.send()
