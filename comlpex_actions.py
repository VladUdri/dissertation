import pyautogui as pg
from time import sleep
from key_action import KeyAction
from speak import Speak
from vost_text import VoskModell
from word2number import w2n


class ComplexAction:
    def __init__(self) -> None:
        # self.actions = actions
        self.key_action = KeyAction()

    def execute(self, commands, key):
        for comm in commands[key]['steps']:
            if comm == 'listen_int':
                Speak().simple_speak(commands[key]['speak'])
                res = VoskModell().listen_for_commands(True)
                int_res = w2n.word_to_num(res)
                pg.write(str(int_res))
            elif comm == 'listen_word':
                Speak().simple_speak(commands[key]['speak'])
                res = VoskModell().listen_for_commands(True)
                pg.write(res)
            elif comm == 'execute':
                self.key_action.execute(commands[key]['execute'])
            else:
                print(commands[comm]['execute'])
                self.key_action.execute(commands[comm]['execute'])
        pg.press('enter')
        # print(commands)
        # self.key_action.execute()
