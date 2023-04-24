import pyautogui as pg
from time import sleep


class KeyAction:
    def __init__(self) -> None:
        pass

    def execute(self, actions):
        try:
            # loop over the actions list, 2 elements at a time
            for index in range(0, len(actions), 2):
                # if the current action is "press", simulate a key press using pyautogui (the key is the next element)
                if actions[index] == 'press':
                    pg.press(actions[index + 1])
                # if the current action is "key_down", simulate a key down using pyautogui (the key is the next element)
                elif actions[index] == 'key_down':
                    pg.keyDown(actions[index + 1])
                # if the current action is "key_up", simulate a key up using pyautogui (the key is the next element)
                elif actions[index] == 'key_up':
                    pg.keyUp(actions[index + 1])
                # if the current action is an integer, it means the key needs to be pressed more than once
                elif isinstance(actions[index], int):
                    # simulate pressing the keys for a certain number of times using pyautogui
                    pg.press(keys=actions[index + 1], presses=actions[index])
                # wait for 0.1 seconds between each action
                sleep(0.1)

            # return True if all actions were successfully executed
            return True
        except Exception as e:
            return False
