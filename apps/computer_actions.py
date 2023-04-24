import screen_brightness_control as sbc
from time import sleep
import pyautogui as pg
from one_answer_listener import OneAnswerListener
from word2number import w2n
from speak import Speak
from application import IApplications


class ComputerActions(IApplications):
    def __init__(self, _app_name='computer_action'):
        super().__init__(_app_name)

    def computer_brightness_value(self):
        # Ask for the desired brightness value and set it
        Speak().simple_speak('What should be the brightness value?')
        value = OneAnswerListener().listen_for_commands(True)
        int_value = w2n.word_to_num(value)
        sbc.set_brightness(int_value)
        return True

    def computer_brightness_down(self):
        # Decrease the brightness value by 10, if possible
        current_value = sbc.get_brightness()
        if current_value[0] == 0:
            Speak().simple_speak('Brightness value is already at minimum')
            return False
        else:
            sbc.set_brightness(current_value[0] - 10)
            sleep(1)
            return True

    def computer_brightness_up(self):
        # Increase the brightness value by 10, if possible
        current_value = sbc.get_brightness()
        if current_value[0] == 100:
            Speak().simple_speak('Brightness value is already at maximum')
            return False
        else:
            sbc.set_brightness(current_value[0] + 10)
            sleep(1)
            return True


    def computer_volume_value(self):
        # Asks user to specify the volume value
        Speak().simple_speak('What should be the volume value?')
        # Listens for user input
        value = OneAnswerListener().listen_for_commands(True)
        pg.press('volumedown', presses=50)
        # Converts the user input to an integer value
        int_value = w2n.word_to_num(value)
        pg.press('volumeup', presses=int(int_value / 2))

def computer_volume_up(self):
    # Increases the volume by pressing volume up key 5 times
    pg.press('volumeup', presses=5)
    sleep(0.2)

def computer_volume_down(self):
    # Decreases the volume by pressing volume down key 5 times
    pg.press('volumedown', presses=5)
    sleep(0.2)

