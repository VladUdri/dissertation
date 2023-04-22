from application import IApplications
import pyautogui as pg
from time import sleep
from speak import Speak
from utils import focus_window
from one_answer_listener import Voicev
from commands.vosk_dictation import VoskDictation
from word2number import w2n


class Outlook(IApplications):
    def __init__(self, app_name='outlook'):
        super().__init__(app_name)

    def outlook_email_create_new(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', '1',
                                 'key_up', 'ctrl'])
        sleep(0.5)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    def outlook_email_send(self):
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                 'key_up', 'alt'])
        sleep(0.1)

    def outlook_email_add_subject(self):

        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt'])
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'a', 'key_up', 'ctrl', 'press', 'backspace'])
        subject = Voicev(
            'What should be the subject?').listen_for_commands(True)
        pg.write(subject)

    def outlook_email_add_to(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        to = Voicev('Say the contact').listen_for_commands(True)
        pg.write(to)
        try:
            sleep(1)
            if pg.locateOnScreen('images\mail.png', grayscale=True, confidence=0.8) is not None:
                res = Voicev(
                    'Please say the number coresponding to your choice').listen_for_commands(True)
                int_res = w2n.word_to_num(res)
                int_res -= 1
                self.key_action.execute([int_res, "down", "press", "enter"])
            else:
                Speak().simple_speak('Could not find contact!')

        except:
            Speak().simple_speak('Something went wrong!')

    def outlook_email_add_cc(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        cc = Voicev('Say the contact').listen_for_commands(True)
        pg.write(cc)
        try:
            sleep(1)
            if pg.locateOnScreen('images\mail_cc.png', grayscale=True, confidence=0.8) is not None:
                res = Voicev(
                    'Please say the number coresponding to your choice').listen_for_commands(True)
                int_res = w2n.word_to_num(res)
                int_res -= 1
                self.key_action.execute([int_res, "down", "press", "enter"])
            else:
                Speak().simple_speak('Could not find contact!')
        except:
            Speak().simple_speak('Something went wrong!')

    def outlook_email_add_body(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                 'key_up', 'alt', 'press', 'tab'])
        self.speak.simple_speak(
            'The dictation will start. To stop it say stop dictationg')
        VoskDictation().execute()

    def _open_calendar(self):
        self.key_action.execute(['key_down', 'ctrl', 'press', '2',
                                 'key_up', 'ctrl'])
        sleep(0.5)

    # added
    def outlook_event_add_title(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'l',
                                 'key_up', 'alt'])
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'a', 'key_up', 'ctrl', 'press', 'backspace'])
        title = Voicev('What should be the title?').listen_for_commands(True)
        pg.write(title)

    # added
    def outlook_event_add_start_time(self):
        self.key_action.execute(['key_down', 'alt', 'press', 't',
                                 'key_up', 'alt'])
        start_date = Voicev(
            'What is the start date?').listen_for_commands(True)
        pg.write(start_date)
        self.key_action.execute(['press', 'enter'])
        start_time = Voicev(
            'What is the start time?').listen_for_commands(True)
        pg.write(start_time)
        self.key_action.execute(['press', 'enter'])

    # added
    def outlook_event_add_end_time(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'd',
                                 'key_up', 'alt'])
        end_date = Voicev('What is the end date?').listen_for_commands(True)
        pg.write(end_date)
        self.key_action.execute(['press', 'enter'])
        end_time = Voicev('What is the end time?').listen_for_commands(True)
        pg.write(end_time)
        self.key_action.execute(['press', 'enter'])

    # added
    def outlook_event_save(self):
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                 'key_up', 'alt'])

    # added
    def outlook_event_make_event_all_day(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'y',
                                 'key_up', 'alt'])

    def outlook_event_add_body(self):
        self.key_action.execute(['key_down', 'alt', 'press', 'l',
                                 'key_up', 'alt', 12, 'tab'])
        self.speak.simple_speak(
            'The dictation will start. To stop it say stop dictationg')
        VoskDictation().execute()

    def outlook_create_event(self):
        focus_window(self._app_name)
        sleep(0.5)
        self._open_calendar()
        sleep(0.5)
        self.create_new()
        sleep(0.5)
