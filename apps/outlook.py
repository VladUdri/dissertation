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
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    def outlook_email_send(self):
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                 'key_up', 'alt'])
        sleep(0.1)

    def outlook_email_add_subject(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt'])
        subject = Voicev().listen_for_commands(True)
        pg.write(subject)
        print('done')

    def outlook_email_add_to(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        VoskDictation().execute()
        # pg.write(to)??
        print('done')

    def outlook_email_add_cc(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        cc = Voicev().listen_for_commands(True)
        pg.write(cc)
        print('done')

    def outlook_email_add_body(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'press', 'tab'])
        VoskDictation().execute()
        print('done')

    # def outlook_send_email(self):
    #     self.key_action.execute(['key_down', 'ctrl', 'press', '1',
    #                              'key_up', 'ctrl'])
    #     self.create_new()
    #     sleep(1)
    #     self.speak.simple_speak(
    #         'Who do you want to send the email to?')
    #     to = Voicev().listen_for_commands(True)
    #     pg.write(to)
    #     sleep(1)
    #     pg.press('tab')
    #     sleep(0.5)
    #     pg.press('tab')
    #     self.speak.simple_speak(
    #         'Who shoud be as cc\'s')
    #     cc = Voicev().listen_for_commands(True)
    #     if cc != 'none' and cc != 'nobody':
    #         pg.write(cc)
    #     sleep(0.5)
    #     pg.press('tab')
    #     self.speak.simple_speak(
    #         'What should be the subject?')
    #     subject = Voicev().listen_for_commands(True)
    #     pg.write(subject)
    #     sleep(0.5)
    #     pg.press('tab')
    #     self.speak.simple_speak(
    #         'Please start dictating. When you are done, just say stop dictating!')
    #     VoskDictation().execute()
    #     sleep(1)
    #     # self.send()

    def open_calendar(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', '2',
                                 'key_up', 'ctrl'])
        sleep(0.5)

    # added
    def add_title_event(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'l',
                                 'key_up', 'alt'])
        title = Voicev().listen_for_commands(True)
        pg.write(title)
        print('done')

    # added
    def event_add_start_time(self):
        self.key_action.execute(['key_down', 'alt', 'press', 't',
                                 'key_up', 'alt'])
        start_date = Voicev().listen_for_commands(True)
        pg.write(start_date)
        self.key_action.execute(['press', 'enter'])
        start_time = Voicev().listen_for_commands(True)
        pg.write(start_time)
        self.key_action.execute(['press', 'enter'])
        print('done')

    # added
    def event_add_end_time(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'd',
                                 'key_up', 'alt'])
        end_date = Voicev().listen_for_commands(True)
        pg.write(end_date)
        self.key_action.execute(['press', 'enter'])
        end_time = Voicev().listen_for_commands(True)
        pg.write(end_time)
        self.key_action.execute(['press', 'enter'])
        print('done')

    # added
    def event_save(self):
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                 'key_up', 'alt'])
        print('done')

    # added
    def event_make_event_all_day(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'y',
                                 'key_up', 'alt'])
        print('done')

    #
    def event_make_event_all_day(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'y',
                                 'key_up', 'alt'])
        print('done')

    def event_add_body(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'l',
                                 'key_up', 'alt', 12, 'tab'])
        pg.write('asdasdasdasdasd')

        print('done')

    def outlook_create_event(self):
        focus_window(self._app_name)
        sleep(0.5)
        self.open_calendar()
        sleep(0.5)
        self.create_new()
        self.speak.simple_speak('Event created')