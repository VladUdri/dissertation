import pyautogui as pg
from time import sleep


class KeyAction:
    def __init__(self) -> None:
        # self.actions = actions
        pass

    def execute(self, actions):
        try:
            for index in range(0, len(actions), 2):
                if actions[index] == 'press':
                    pg.press(actions[index + 1])
                elif actions[index] == 'key_down':
                    pg.keyDown(actions[index + 1])
                elif actions[index] == 'key_up':
                    pg.keyUp(actions[index + 1])
                elif isinstance(actions[index], int):
                    pg.press(keys=actions[index + 1], presses=actions[index])
                sleep(0.1)
            return True
        except Exception as e:
            print('exception', e)
            return False
