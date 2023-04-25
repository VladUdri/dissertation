from application import IApplications
import pyautogui as pg
from time import sleep
from speak import Speak
from utils import focus_window
from one_answer_listener import OneAnswerListener
from commands.vosk_dictation import VoskDictation
from word2number import w2n


class Outlook(IApplications):
    # Constructor method for the class.
    # Takes app_name as an argument and initializes the parent class.
    def __init__(self, app_name='outlook'):
        super().__init__(app_name)

    # Method for creating a new email in Outlook.
    def outlook_email_create_new(self):
        # Presses the key combination for creating a new email.
        self.key_action.execute(['key_down', 'ctrl', 'press', '1',
                                'key_up', 'ctrl'])
        sleep(0.5)
        # Presses the key combination for creating a new email.
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                'key_up', 'ctrl'])

    # Method for sending an email in Outlook.
    def outlook_email_send(self):
        # Presses the key combination for sending an email.
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                'key_up', 'alt'])
        sleep(0.1)

    # Method for adding a subject to the email.
    def outlook_email_add_subject(self):
        # Presses the key combination for opening the subject field.
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                'key_up', 'alt'])
        # Presses the key combination for selecting all the text in the subject field and deleting it.
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'a', 'key_up', 'ctrl', 'press', 'backspace'])
        # Gets the subject for the email from the user and writes it using pyautogui.
        subject = OneAnswerListener(
            'What should be the subject?').listen_for_commands(True)
        pg.write(subject)

    # Method for adding the recipient of the email.
    def outlook_email_add_to(self):
        # Presses the key combination for opening the "To" field.
        self.key_action.execute(['key_down', 'alt', 'press', 'u',
                                'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        # Gets the recipient's email address from the user and writes it using pyautogui.
        to = OneAnswerListener('Say the contact').listen_for_commands(True)
        pg.write(to)
        try:
            sleep(1)
            # If an image of the recipient's email address is found, selects it.
            if pg.locateOnScreen('images\mail.png', grayscale=True, confidence=0.8) is not None:
                # Asks the user for the number corresponding to the correct email address and selects it.
                res = OneAnswerListener(
                    'Please say the number corresponding to your choice').listen_for_commands(True)
                int_res = w2n.word_to_num(res)
                int_res -= 1
                self.key_action.execute([int_res, "down", "press", "enter"])
            else:
                # If the image of the recipient's email address is not found, informs the user.
                Speak().simple_speak('Could not find contact!')

        except:
            # If an error occurs, informs the user.
            Speak().simple_speak('Something went wrong!')

    def outlook_email_add_cc(self):
        # This method adds a contact to the CC field of an email in Outlook.
        # It uses keyboard shortcuts to navigate to the CC field, listens for user input, and types in the contact name.
        self.key_action.execute(['key_down', 'alt', 'press', 'u',  # Pressing Alt+U opens the CC field
                                # Pressing Shift+Tab selects the To field
                                 'key_up', 'alt', 'key_down', 'shift', 'press', 'tab',
                                 'key_up', 'shift'])
        # Listening for user input to enter the contact's name
        cc = OneAnswerListener('Say the contact').listen_for_commands(True)
        # Typing in the contact's name using pyautogui
        pg.write(cc)
        try:
            sleep(1)
            # Checking if the contact was successfully added by searching for a specific image on the screen
            if pg.locateOnScreen('images\mail_cc.png', grayscale=True, confidence=0.8) is not None:
                # If the image is found, asking the user to choose the correct contact from a list
                res = OneAnswerListener(
                    'Please say the number corresponding to your choice').listen_for_commands(True)
                # Converting the user's spoken number to an integer
                int_res = w2n.word_to_num(res)
                int_res -= 1  # Subtracting 1 because the list is zero-indexed
                # Selecting the contact from the list using keyboard shortcuts
                self.key_action.execute([int_res, "down", "press", "enter"])
            else:
                # If the image is not found, notifying the user that the contact could not be added
                Speak().simple_speak('Could not find contact!')
        except:
            # If an error occurs, notifying the user that something went wrong
            Speak().simple_speak('Something went wrong!')

    def outlook_email_add_body(self):
        # This method adds text to the body of an email in Outlook.
        # It uses keyboard shortcuts to navigate to the body field, prompts the user to start dictating text, and uses voice recognition to convert spoken text to written text.
        self.key_action.execute(['key_down', 'alt', 'press', 'u',  # Pressing Alt+U opens the body field
                                'key_up', 'alt', 'press', 'tab'])
        # Prompting the user to start dictating text
        self.speak.simple_speak(
            'The dictation will start. To stop it say stop dictationg')
        # Starting the dictation process using the VoskDictation class
        VoskDictation().execute()

    def _open_calendar(self):
        # This method opens the calendar in Outlook.
        # It uses keyboard shortcuts to navigate to the calendar.
        self.key_action.execute(['key_down', 'ctrl', 'press', '2',  # Pressing Ctrl+2 opens the calendar
                                'key_up', 'ctrl'])
        sleep(0.5)

    def outlook_event_add_title(self):
        # This method adds a title to an event in the Outlook calendar.
        # It uses keyboard shortcuts to navigate to the title field, prompts the user to enter a title, and types in the title using pyautogui.
        self.key_action.execute(['key_down', 'alt', 'press', 'l',  # Pressing Alt+L opens the title field
                                'key_up', 'alt'])
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'a', 'key_up', 'ctrl', 'press', 'backspace'])
        title = OneAnswerListener(
            'What should be the title?').listen_for_commands(True)
        pg.write(title)

    def outlook_event_add_start_time(self):
        # Press the 'Alt + T' key combination to open the start time field
        self.key_action.execute(['key_down', 'alt', 'press', 't',
                                'key_up', 'alt'])
        # Prompt the user to input the start date using speech-to-text
        start_date = OneAnswerListener(
            'What is the start date?').listen_for_commands(True)
        # Write the start date into the input field
        pg.write(start_date)
        # Press the 'Enter' key to confirm the start date
        self.key_action.execute(['press', 'enter'])
        # Prompt the user to input the start time using speech-to-text
        start_time = OneAnswerListener(
            'What is the start time?').listen_for_commands(True)
        # Write the start time into the input field
        pg.write(start_time)
        # Press the 'Enter' key to confirm the start time
        self.key_action.execute(['press', 'enter'])

    def outlook_event_add_end_time(self):
        # Press the 'Alt + D' key combination to open the end time field
        self.key_action.execute(['key_down', 'alt', 'press', 'd',
                                'key_up', 'alt'])
        # Prompt the user to input the end date using speech-to-text
        end_date = OneAnswerListener(
            'What is the end date?').listen_for_commands(True)
        # Write the end date into the input field
        pg.write(end_date)
        # Press the 'Enter' key to confirm the end date
        self.key_action.execute(['press', 'enter'])
        # Prompt the user to input the end time using speech-to-text
        end_time = OneAnswerListener(
            'What is the end time?').listen_for_commands(True)
        # Write the end time into the input field
        pg.write(end_time)
        # Press the 'Enter' key to confirm the end time
        self.key_action.execute(['press', 'enter'])

    def outlook_event_save(self):
        # Press the 'Alt + S' key combination to save the event
        self.key_action.execute(['key_down', 'alt', 'press', 's',
                                'key_up', 'alt'])

    def outlook_event_make_event_all_day(self):
        # Press the 'Alt + Y' key combination to make the event an all-day event
        self.key_action.execute(['key_down', 'alt', 'press', 'y',
                                'key_up', 'alt'])

    def outlook_event_add_body(self):
        # Press the 'Alt + L' key combination to open the event body field
        # and then press the 'Tab' key 12 times to move to the next field
        self.key_action.execute(['key_down', 'alt', 'press', 'l',
                                'key_up', 'alt', 12, 'tab'])
        # Prompt the user to speak and dictate the event body using a speech recognition engine
        self.speak.simple_speak(
            'The dictation will start. To stop it say stop dictationg')
        VoskDictation().execute()
    
    def outlook_create_event(self):
        # Bring the Outlook window into focus
        focus_window(self._app_name)
        # Wait for 0.5 seconds
        sleep(0.5)
        # Open the calendar window
        self._open_calendar()
        # Wait for 0.5 seconds
        sleep(0.5)
        # Create a new event
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                'key_up', 'ctrl'])
        # Wait for 0.5 seconds
        sleep(0.5)
