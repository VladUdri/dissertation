import pyautogui as pg
from time import sleep
from images.vosk_voice import VoskModel
import json
from key_action import KeyAction
from nltk.tokenize import word_tokenize


class WriteText:
    def __init__(self) -> None:
        with open('write_commands.json') as f:
            self.write_comm = json.load(f)
        self.format = {}
        self.key_action = KeyAction()

    def run_write(self):
        listen = VoskModel()
        needs_response = True
        print(self.write_comm['bold'])
        while needs_response:
            response = next(listen.listen_write())
            if response == 'stop writing':
                break
            self.write_text(response)

    def write_title(self, text):
        self.align_center()
        self.change_to_bold()
        pg.write(text)
        self.change_to_bold()
        sleep(0.1)

    def execute_keypress(self, action):
        self.key_action.execute(self.write_comm[action]['execute'])

    def search_str(self, text):
        for key in self.write_comm:
            for index in range(0, len(self.write_comm[key]['pattern_start'])):
                if self.write_comm[key]['pattern_start'][index] in text:
                    text = text.replace(
                        self.write_comm[key]['pattern_start'][index], self.write_comm[key]['convertion'])
        return text

    def write_text(self, text):
        words = self.search_str(text).split()
        for word in words:
            if word[1:-1] in self.write_comm.keys():
                self.execute_keypress(word[1:-1])
            else:
                pg.write(' ')
                pg.write(word)
