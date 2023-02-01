import pyautogui as pg


class KeyAction:
    def __init__(self, actions) -> None:
        self.actions = actions

    def execute(self):
        for index in range(0, len(self.actions), 2):
            if self.actions[index] == 'press':
                pg.press(self.actions[index + 1])
            elif self.actions[index] == 'key_down':
                pg.keyDown(self.actions[index + 1])
            elif self.actions[index] == 'key_up':
                pg.keyUp(self.actions[index + 1])
