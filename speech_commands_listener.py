"""Class that used Vosk to listen for speech commands given by the user"""

import pytesseract
import json
import sys
import queue
import sounddevice as sd
import vosk
from speak import Speak
from voice_interpreter import VoiceInterpreter
vosk.SetLogLevel(-1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class SpeechCommandListener():
    def __init__(self, stop_command='close application', trigger_command='initialize application'):
        self.model_path = "D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph"
        self.q = queue.Queue()
        self.previous_line = ""
        self.stop_command = stop_command
        self.trigger_command = trigger_command
        self.speaker = Speak()

    def listen_for_commands(self, REC, SAMPLERATE):
        # from main import
        self.speaker.simple_speak(
            'To start the program say initialise application')

        try:
            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):

                fin = new_fin = ''
                # used to stop listeing when the program is processing
                listening = True
                # used to only listen for the trigger word
                waiting_for_commands = False

                # loops to listen for commands
                #
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
                                    if d[key] == self.stop_command:
                                        with open('jsons/last_app/last_app.txt', 'w') as h:
                                            h.write('')
                                        self.speaker.simple_speak('Good bye!')
                                        return
                                    elif d[key] == self.trigger_command and waiting_for_commands == False:
                                        self.speaker.simple_speak('Welcome!')
                                        waiting_for_commands = True
                                        self.q.queue.clear()
                                    self.previous_line = d[key]
                    if waiting_for_commands == True:
                        if fin == new_fin and fin != '' and new_fin != '' and fin != self.trigger_command:
                            try:
                                listening = False
                                # if a command is understood, it is passed to the VoiceInterpreter to be processed
                                res = VoiceInterpreter(self.comm).execute(fin)
                            except:
                                self.speak.simple_speak('I don\'t know that!')
                            else:
                                # Clear the queue for possible commands listened during processing
                                self.q.queue.clear()
                                if res is None:
                                    listening = True
                                fin = new_fin = ''

        except Exception as e:
            print('exception', e)

    def _callback(self, indata, frames, time, status):
        # This is called (from a separate thread) for each audio block.
        if status:
            print(status, file=sys.stderr)
            sys.stdout.flush()
        self.q.put(bytes(indata))
