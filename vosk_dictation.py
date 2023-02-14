import pytesseract
import time
import os
import pyautogui
import json
import sys
import queue
import sounddevice as sd
import vosk
from key_action import KeyAction

vosk.SetLogLevel(-1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class VoskDictation():
    def __init__(self, lang='en', mode='transcription', safety_word='stop listening'):
        self.model_path = "D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph"
        self.q = queue.Queue()
        self.previous_line = ""
        self.previous_length = 0
        self.mode = mode
        self.safety_word = safety_word
        self.lang = lang
        self.rec = ""
        self.text_dict = {}
        self.co_ord_list = []
        self.last_index = -1
        self.first_index = -1
        self.match = False
        with open('write_commands.json') as f:
            self.write_comm = json.load(f)
        self.format = {}
        self.key_action = KeyAction()

    def setUp(self):
        if not os.path.exists(self.model_path):
            print(r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")
            print(f"and unpack into {self.model_path}.")
        # print(self.model_path)
        device_info = sd.query_devices(kind='input')
        samplerate = int(device_info['default_samplerate'])
        model = vosk.Model(self.model_path)
        rec = vosk.KaldiRecognizer(model, samplerate)
        return rec, samplerate

    def transcribe(self):
        rec, samplerate = self.setUp()
        try:

            with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):

                initial = time.perf_counter()
                while True:
                    data = self.q.get()
                    if rec.AcceptWaveform(data):
                        d = json.loads(rec.Result())
                    else:
                        d = json.loads(rec.PartialResult())
                    for key in d.keys():
                        if d[key]:
                            if d[key] != self.previous_line or key == 'text':
                                self._write(d)
                                if d[key] == self.safety_word:
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

    def execute_keypress(self, key):
        self.key_action.execute(self.write_comm[key]['execute'])

    def search_str(self, text):
        for key in self.write_comm:
            for index in range(0, len(self.write_comm[key]['pattern_start'])):
                if self.write_comm[key]['pattern_start'][index] in text:
                    self.execute_keypress(key)
                    return True
        return False

    def _write(self, phrase):
        pyautogui.press('backspace', presses=self.previous_length)
        print(phrase)
        if 'text' in phrase:
            self.previous_length = 0
            if self.search_str(phrase['text']) == False:
                pyautogui.write(phrase['text'] + ' ')

        else:
            pyautogui.write(phrase['partial'])
            self.previous_length = len(phrase['partial'])
