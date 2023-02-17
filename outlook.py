from application import IApplications
import pyautogui as pg
from time import sleep
from utils import focus_window
from voicev import Voicev
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
        self.key_action.execute(['key_down', 'ctrl', 'press', '1',
                                 'key_up', 'ctrl'])
        self.create_new()
        sleep(1)
        self.speak.simple_speak(
            'Who do you want to send the email to?')
        to = Voicev().listen_for_commands(True)
        pg.write(to)
        sleep(1)
        pg.press('tab')
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'Who shoud be as cc\'s')
        cc = Voicev().listen_for_commands(True)
        if cc != 'none' and cc != 'nobody':
            pg.write(cc)
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'What should be the subject?')
        subject = Voicev().listen_for_commands(True)
        pg.write(subject)
        sleep(0.5)
        pg.press('tab')
        self.speak.simple_speak(
            'Please start dictating. When you are done, just say stop dictating!')
        VoskDictation().execute()
        sleep(1)
        # self.send()

    def open_calendar(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', '2',
                                 'key_up', 'ctrl'])

    def create_event(self):
        # if self._state != 'closed':
        focus_window(self._app_name)
        sleep(0.5)
        self.open_calendar()
        sleep(0.5)
        self.create_new()
        self.speak.simple_speak('What should be the title of the event?')
        title = Voicev().listen_for_commands(True)
        pg.write(title)
        self.key_action.execute(['press', 'tab'])
        self.speak.simple_speak(
            'What should be the starting date of the event?')
        starting_date = Voicev().listen_for_commands(True)
        pg.write(starting_date)
        self.key_action.execute(['press', 'tab', 'press', 'tab'])
        self.speak.simple_speak(
            'What should be the starting time of the event?')
        starting_time = Voicev().listen_for_commands(True)
        pg.write(starting_time)

        self.key_action.execute(['press', 'tab'])
        self.speak.simple_speak(
            'What should the the ending date of the event?')
        ending_date = Voicev().listen_for_commands(True)
        pg.write(ending_date)
        self.key_action.execute(['press', 'tab', 'press', 'tab'])
        self.speak.simple_speak(
            'What should be the ending time of the event?')
        ending_time = Voicev().listen_for_commands(True)
        pg.write(ending_time)

        self.key_action.execute(
            ['press', 'tab', 'press', 'tab', 'press', 'tab', 'press', 'tab', 'press', 'tab'])
        self.speak.simple_speak(
            'What should be the location the event?')
        location = Voicev().listen_for_commands(True)
        pg.write(location)
        sleep(0.5)
        self.key_action.execute(['press', 'enter', 'press', 'tab'])
        self.speak.simple_speak(
            'Please tell me more about the event!')  # todo stop word
        VoskDictation().execute()

        self.key_action.execute(
            ['key_down', 'alt', 'press', 's', 'key_up', 'alt'])
