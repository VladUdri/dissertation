import pytesseract
import pyautogui as pg
import json
import sys
import queue
import sounddevice as sd
import vosk
from key_action import KeyAction
from comlpex_actions import ComplexAction
vosk.SetLogLevel(-1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class VoskDictation():
    def __init__(self, safety_word='stop dictating'):
        self.q = queue.Queue()
        self.previous_line = ""
        self.previous_length = 0
        self.safety_word = safety_word
        with open('jsons/write_commands.json') as f:
            self.write_comm = json.load(f)
        self.key_action = KeyAction()
        self.complex_action = ComplexAction()
        self.listening = True
        with open('jsons/last_app/last_app.txt') as h:
            self.last_app = h.readlines()

    def execute(self):
        from main import REC, SAMPLERATE

        try:

            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):

                while True:
                    if self.listening == True:
                        data = self.q.get()
                        if REC.AcceptWaveform(data):

                            d = json.loads(REC.Result())
                        else:
                            d = json.loads(REC.PartialResult())

                        for key in d.keys():
                            if d[key]:
                                if d[key] != self.previous_line or key == 'text':
                                    self._write(d)
                                    if isinstance(self.last_app, list):
                                        if self.last_app[0] == 'notepad':
                                            pg.write(' ')
                                            pg.press('backspace')
                                    else:
                                        if self.last_app == 'notepad':
                                            pg.write(' ')
                                            pg.press('backspace')
                                    if d[key] == self.safety_word:
                                        self.key_action.execute(
                                            ['key_down', 'ctrl', 2, 'backspace', 'key_up', 'ctrl'])
                                        return
                                    self.previous_line = d[key]
        except KeyboardInterrupt:
            print('\nDone -- KEYBOARDiNTERRUPT')
        except Exception as e:
            print('exception', e)

    def _callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
            sys.stdout.flush()
        self.q.put(bytes(indata))

    def _search_str(self, text):
        for key in self.write_comm:
            for index in range(0, len(self.write_comm[key]['pattern'])):
                if self.write_comm[key]['pattern'][index] == text:
                    return key
        return False

    def _write(self, phrase):
        pg.press('backspace', presses=self.previous_length)

        if 'text' in phrase:
            search_res = self._search_str(phrase['text'])
            self.previous_length = 0

            if search_res == False:
                pg.write(phrase['text'] + ' ')
            else:
                if self.write_comm[search_res]['type'] == 'key':
                    self.listening = False
                    pg.press('backspace')
                    execution_res = self.key_action.execute(
                        self.write_comm[search_res]['execute'])
                    if execution_res:
                        self.listening = True
                elif self.write_comm[search_res]['type'] == 'complex_action':
                    self.listening = self.complex_action.execute(
                        self.write_comm, search_res)
                elif self.write_comm[search_res]['type'] == 'action':
                    self.listening = False
                    self.listening = self.key_action.execute(
                        self.write_comm[search_res]['execute'])
            self.q.queue.clear()

        else:
            pg.write(phrase['partial'])
            self.previous_length = len(phrase['partial'])
