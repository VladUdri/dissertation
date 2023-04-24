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

        # Importing REC and SAMPLERATE from main module
        from main import REC, SAMPLERATE

        try:
            # Recording voice input using sd.RawInputStream method
            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):

                # Running an infinite loop until break statement
                while True:
                    # Checking if listening is True
                    if self.listening == True:
                        # Getting data from queue
                        data = self.q.get()

                        # Checking if the waveform is accepted or partially accepted
                        if REC.AcceptWaveform(data):
                            d = json.loads(REC.Result())
                        else:
                            d = json.loads(REC.PartialResult())

                        # Checking keys in dictionary and performing actions based on their values
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

                                    # Checking if the safety word is spoken
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
        # Uses pyautogui to press the backspace key n times to remove the previously written text
        pg.press('backspace', presses=self.previous_length)

        # Checks if the 'text' key is in the given phrase
        if 'text' in phrase:
            # Searches for the text in the 'write_commands.json' file using the _search_str() method
            search_res = self._search_str(phrase['text'])

            # Resets the previous_length counter to 0
            self.previous_length = 0

            # If the search result is False, writes the dictated text and a space
            if search_res == False:
                pg.write(phrase['text'] + ' ')

            # If the search result is not False
            else:
                # If the command is a key press, executes the command using the KeyAction class and pyautogui,
                # then sets listening to True
                if self.write_comm[search_res]['type'] == 'key':
                    self.listening = False
                    pg.press('backspace')
                    execution_res = self.key_action.execute(
                        self.write_comm[search_res]['execute'])
                    if execution_res:
                        self.listening = True
                # If the command is a complex action, executes the command using the ComplexAction class,
                # then sets listening to the return value of the execute() method
                elif self.write_comm[search_res]['type'] == 'complex_action':
                    self.listening = self.complex_action.execute(
                        self.write_comm, search_res)
                # If the command is a regular action, executes the command using the KeyAction class and pyautogui,
                # then sets listening to True
                elif self.write_comm[search_res]['type'] == 'action':
                    self.listening = False
                    self.listening = self.key_action.execute(
                        self.write_comm[search_res]['execute'])

            # Clears the queue
            self.q.queue.clear()

        # If the 'text' key is not in the given phrase, writes the partial text using pyautogui,
        # then sets the previous_length counter to the length of the partial text
        else:
            pg.write(phrase['partial'])
            self.previous_length = len(phrase['partial'])
