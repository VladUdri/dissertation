import screen_brightness_control as sbc
from time import sleep
import pyautogui as pg
from voicev import Voicev
from word2number import w2n
from speak import Speak
from application import IApplications


class ComputerActions(IApplications):
    def __init__(self, _app_name='computer_action', state=''):
        super().__init__(_app_name, state)

    def create_new(self):
        return super().create_new()

    def computer_brightness_value(self):
        Speak().simple_speak('What should be the brightness value?')
        value = Voicev().listen_for_commands(True)
        int_value = w2n.word_to_num(value)
        sbc.set_brightness(int_value)
        print('Brightness changed to ' + value + '!')
        return True

    def computer_brightness_down(self):
        current_value = sbc.get_brightness()
        if current_value[0] == 0:
            Speak().simple_speak('Brightness value is already at minimum')
            print('Brightness value is already at min')
            return False
        else:
            sbc.set_brightness(current_value[0] - 10)
            sleep(1)
            print('Brightness down!')
            return True

    def computer_brightness_up(self):
        current_value = sbc.get_brightness()
        if current_value[0] == 100:
            print('Brightness value is already at max')
            Speak().simple_speak('Brightness value is already at maximum')
            return False
        else:
            sbc.set_brightness(current_value[0] + 10)
            sleep(1)
            print('Brightness up!')
            return True

    def computer_volume_value(self):
        Speak().simple_speak('What should be the volume value?')
        value = Voicev().listen_for_commands(True)
        pg.press('volumedown', presses=50)
        int_value = w2n.word_to_num(value)
        pg.press('volumeup', presses=int(int_value / 2))
        print('Volume set at ' + value + '%!')

    def computer_volume_up(self):
        pg.press('volumeup', presses=5)
        sleep(0.2)
        if pg.locateCenterOnScreen('img\\volume_max.png'):
            print('Maximum volume')
            Speak().simple_speak('Volume is at maximum!')

    def computer_volume_down(self):
        pg.press('volumedown', presses=5)
        sleep(0.2)
        if pg.locateCenterOnScreen('img\\volume_zero.png'):
            print('Minimum volume')
            Speak().simple_speak('Volume is at minimum!')
