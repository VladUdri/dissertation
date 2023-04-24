import pyautogui as pg
from time import sleep
from key_action import KeyAction
from speak import Speak
from one_answer_listener import OneAnswerListener
from word2number import w2n


class ComplexAction:
    def __init__(self) -> None:
        self.key_action = KeyAction()
        
    # Method to execute commands
    def execute(self, commands, key):
        try:
            # Loop through each command in the list of steps for the given key
            for comm in commands[key]['steps']:
                # If the command is 'listen_int'
                if comm == 'listen_int':
                    Speak().simple_speak(commands[key]['speak'])
                    # Listen for a command and convert the spoken number to an integer
                    res = OneAnswerListener().listen_for_commands(True)
                    int_res = w2n.word_to_num(res)
                    # Type the integer value on the keyboard
                    pg.write(str(int_res))
                # If the command is 'listen_word'
                elif comm == 'listen_word':
                    Speak().simple_speak(commands[key]['speak'])
                    # Listen for a command and type the spoken word on the keyboard
                    res = OneAnswerListener().listen_for_commands(True)
                    pg.write(res)
                # If the command is 'execute'
                elif comm == 'execute':
                    # Execute a series of key actions
                    self.key_action.execute(commands[key]['execute'])
                else:
                    # Execute a series of key actions for another command
                    print(commands[comm]['execute'])
                    self.key_action.execute(commands[comm]['execute'])
            # Press 'Enter' on the keyboard
            pg.press('enter')
            return True
        except:
            return False