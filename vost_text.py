import pytesseract
import time
import os
import pyautogui
import json
import sys
import queue
import sounddevice as sd
import vosk

vosk.SetLogLevel(-1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class VoskModell():
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

#######################################################################
    def listen_for_commands(self, one_time):
        rec, samplerate = self.setUp()
        try:

            with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):

                initial = time.perf_counter()
                fin = new_fin = ''
                listening = True
                while True:
                    if listening == True:
                        data = self.q.get()
                        if rec.AcceptWaveform(data):
                            d = json.loads(rec.Result())
                        else:
                            d = json.loads(rec.PartialResult())
                        for key in d.keys():
                            if d[key]:
                                if d[key] != self.previous_line or key == 'text':
                                    if "text" in d:
                                        fin = new_fin
                                        new_fin = d["text"]
                                    else:
                                        fin = new_fin
                                        new_fin = d["partial"]
                                    if d[key] == self.safety_word:
                                        return
                                    self.previous_line = d[key]
                    if (fin == new_fin and fin != '' and new_fin != ''):
                        listening = False
                        # use fin
                        if one_time == True:
                            return fin
                        print(fin)
                        fin = new_fin = ''

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
