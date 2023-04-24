from application import IApplications
import pyautogui as pg
from time import sleep
from utils import focus_window
from one_answer_listener import OneAnswerListener
from word2number import w2n
from speak import Speak


class Word(IApplications):
    def __init__(self, app_name='word'):
        super().__init__(app_name)

    # Creates a new Word document
    def word_create_new(self):
        focus_window(self._app_name)  # focuses on the Word application window
        # presses the key combination to create a new document
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'n', 'key_up', 'ctrl'])

    # Creates a new blank Word document
    def word_create_new_blank(self):
        # focuses on the Word application window
        focus_window(self._app_name)
        # presses the key combination to create a new blank document
        self.key_action.execute(['press', 'alt', 'press', 'n', 'press', 'l'])
        sleep(2)

    # Saves the current Word document with a specified name
    def word_save_as(self):
        # focuses on the Word application window
        focus_window(self._app_name)
        # presses the key combination to open the save as dialog
        self.key_action.execute(
            ['press', 'alt', 'press', 'f', 'press', 'a', 'press', 'o'])
        sleep(1)
        self._save_replace()  # helper method to handle saving with a name that already exists

    # Helper method to handle saving with a name that already exists
    def _save_replace(self):
        name = OneAnswerListener('What should be the name of the document?').listen_for_commands(
            True)  # listens for the name to save the document with
        pg.write(name)  # types the name into the save as dialog
        sleep(1)
        # presses enter to save the document with the given name
        self.key_action.execute(['press', 'enter'])
        sleep(1)
        # checks if the 'Save As' dialog with the option to replace the existing document is visible
        if pg.locateOnScreen('images\save_replace.png', grayscale=True, confidence=0.8) is not None:
            # asks the user if they want to replace the existing document
            self.speak.simple_speak(
                'This already exists! Do you want to replace it?')
            response = OneAnswerListener().listen_for_commands(True)
            if response == 'yes':  # if user says yes, replaces the existing document
                self.key_action.execute(['press', 'enter'])
            elif response == 'no':  # if user says no, selects the option to not replace and tries again
                self.key_action.execute(['press', 'down', 'press', 'enter'])
                self._save_replace()

    # Changes the font of the selected text in the Word document
    def word_change_font(self):
        # focuses on the Word application window
        focus_window(self._app_name)
        # presses the key combination to open the font dialog
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(1)
        font = OneAnswerListener('What should be the new font?').listen_for_commands(
            True)  # listens for the new font name
        sleep(0.5)
        # types the new font name into the font dialog
        pg.write(font)
        sleep(0.5)
        # presses enter to confirm the font change
        pg.press('enter')

    def word_change_size(self):
        # Focuses on the Word window.
        focus_window(self._app_name)
        sleep(1)
        # Presses the keyboard shortcut 'ctrl+d' to open the Font dialog box.
        self.key_action.execute(
            ['key_down', 'ctrl', 'press', 'd', 'key_up', 'ctrl'])
        sleep(0.5)
        # Presses the keyboard shortcut 'alt+s' to navigate to the 'Size' field.
        self.key_action.execute(
            ['key_down', 'alt', 'press', 's', 'key_up', 'alt'])
        int_size = None
        # Loops until the user provides a valid size input.
        while int_size is None:
            try:
                # Asks the user for the new size using voice recognition and
                # converts the input into an integer.
                size = OneAnswerListener(
                    'What should be the new size?').listen_for_commands(True)
                int_size = w2n.word_to_num(size)
                sleep(0.5)
            except:
                # Informs the user that the input was not recognized and asks for the input again.
                Speak().simple_speak('Please say the size again!')
                int_size = None
        # Writes the new size value as a string and presses the 'enter' key to confirm the change.
        pg.write(str(int_size))
        sleep(0.5)
        pg.press('enter')
