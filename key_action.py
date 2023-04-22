import pyautogui as pg
from time import sleep


class KeyAction:
    def __init__(self) -> None:
        pass

    def execute(self, actions):
        print(actions)
        try:
            for index in range(0, len(actions), 2):
                if actions[index] == 'press':
                    pg.press(actions[index + 1])
                elif actions[index] == 'key_down':
                    pg.keyDown(actions[index + 1])
                elif actions[index] == 'key_up':
                    pg.keyUp(actions[index + 1])
                elif isinstance(actions[index], int):
                    print(actions[index])
                    pg.press(keys=actions[index + 1], presses=actions[index])
                sleep(0.1)
            if actions[len(actions)-2] == 'key_down':
                print('yep...')
                pg.keyUp(actions[len(actions) - 1])

            return True
        except Exception as e:
            print('exception', e)
            return False
