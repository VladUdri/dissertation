import screen_brightness_control as sbc
from time import sleep
import pyautogui as pg


class ComputerActions:
    def change_brightness_to(self, value):
        sbc.set_brightness(value)
        print('Brightness changed to ' + value + '!')

    def brightness_down(self):
        current_value = sbc.get_brightness()
        if current_value[0] == 0:
            print('Brightness value is already at min')
        else:
            sbc.set_brightness(current_value[0] - 10)
            sleep(1)
            print('Brightness down!')

    def brightness_up(self):
        current_value = sbc.get_brightness()
        if current_value[0] == 100:
            print('Brightness value is already at max')
        else:
            sbc.set_brightness(current_value[0] + 10)
            sleep(1)
            print('Brightness up!')

    def change_volume_to(self, value):
        pg.press('volumedown', presses=50)
        pg.press('volumeup', presses=int(value / 2))
        print('Volume set at ' + value + '%!')

    def volume_up(self):
        pg.press('volumeup', presses=5)
        sleep(0.2)
        if pg.locateCenterOnScreen('img\\volume_max.png'):
            print('Maximum volume')

    def volume_down(self):
        pg.press('volumedown', presses=5)
        sleep(0.2)
        if pg.locateCenterOnScreen('img\\volume_zero.png'):
            print('Minimum volume')

    def next_track(self):
        pg.press('nexttrack')

    def prev_track(self):
        pg.press('prevtrack')

    def play_pause(self):
        pg.press('playpause')

            # print('Minimum volume')
