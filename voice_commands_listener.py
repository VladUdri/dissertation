import pytesseract
import json
import sys
import queue
import sounddevice as sd
import vosk
from voice_interpretor import VoiceInterpretor

vosk.SetLogLevel(-1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class VoiceCommandListener():
    def __init__(self, safety_word='stop listening'):
        self.model_path = "D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph"
        self.q = queue.Queue()
        self.previous_line = ""
        self.safety_word = safety_word

#######################################################################

    def listen_for_commands(self, one_time=False):
        from main import REC, SAMPLERATE
        print(REC)
        print(SAMPLERATE)
        try:

            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self.__callback):

                fin = new_fin = ''
                listening = True
                while True:
                    if listening == True:
                        data = self.q.get()
                        if REC.AcceptWaveform(data):
                            d = json.loads(REC.Result())
                        else:
                            d = json.loads(REC.PartialResult())
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
                        # listening = False
                        res = VoiceInterpretor().execute(fin)
                        print(fin)
                        if res:
                            listening = True
                        if one_time == True:
                            return fin
                        print(fin)
                        fin = new_fin = ''

        except KeyboardInterrupt:
            print('\nDone -- KEYBOARDiNTERRUPT')
        except Exception as e:
            print('exception', e)

    def __callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
            sys.stdout.flush()
        self.q.put(bytes(indata))
