from application import IApplications
import pyautogui as pg
from time import sleep
from utils import focus_window
from one_answer_listener import OneAnswerListener


class Notepad(IApplications):
    def __init__(self, _app_name='notepad'):
        super().__init__(_app_name)

    # Create a new notepad window
    def notepad_create_new(self):
        focus_window(self._app_name)
        self.key_action.execute(['key_down', 'ctrl', 'press', 'n',
                                 'key_up', 'ctrl'])

    # Save the current notepad file as a new file
    def notepad_save_as(self):
        # Open the save as dialog
        self.key_action.execute(['press', 'alt', 'press', 'f',
                                 'press', 'a'])
        # Call the save and replace function
        self._save_replace()

    # Save the notepad file and replace if the file already exists
    def _save_replace(self):
        # Ask the user for the name of the file to save
        name = OneAnswerListener(
            'What should be the name of the note?').listen_for_commands(True)
        # Write the name of the file to the save dialog
        pg.write(name)
        sleep(1)
        # Press enter to save the file
        self.key_action.execute(['press', 'enter'])
        sleep(1)
        # If a warning dialog appears, ask the user whether to replace the file or not
        if pg.locateOnScreen('images\warning.png') is not None:
            self.speak.simple_speak(
                'This already exists! Do you want to replace it?')
            response = OneAnswerListener().listen_for_commands(True)
            if response == 'yes':
                # If the user says "yes", replace the file
                self.key_action.execute(['press', 'left', 'press', 'enter'])
            elif response == 'no':
                # If the user says "no", do not replace the file and ask again for the name of the file
                self.key_action.execute(['press', 'right', 'press', 'enter'])
                self._save_replace()
