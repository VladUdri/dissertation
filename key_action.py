import pyautogui as pg
from time import sleep


class KeyAction:
    def __init__(self) -> None:
        # self.actions = actions
        pass

    def execute(self, actions):

        for index in range(0, len(actions), 2):
            if actions[index] == 'press':
                pg.press(actions[index + 1])
            elif actions[index] == 'key_down':
                pg.keyDown(actions[index + 1])
            elif actions[index] == 'key_up':
                pg.keyUp(actions[index + 1])
            # sleep(0.5)