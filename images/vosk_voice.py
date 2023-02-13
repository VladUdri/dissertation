import pyaudio
from vosk import Model, KaldiRecognizer
import pytesseract
from time import sleep
# from execution import execute_app
from speak import Speak


class VoskModel:
    def __init__(self) -> None:
        self.speak = Speak()
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.__model = Model(
            r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")
        self.__recognizer = KaldiRecognizer(self.__model, 16000)
        self.mic = pyaudio.PyAudio()
        self.__stream = self.mic.open(format=pyaudio.paInt16, channels=1,
                                      rate=16000, input=True, frames_per_buffer=8192)

    def listen_command(self, commands):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.__model = Model(
            r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")
        self.__recognizer = KaldiRecognizer(self.__model, 16000)
        self.mic = pyaudio.PyAudio()
        self.__stream = self.mic.open(format=pyaudio.paInt16, channels=1,
                                      rate=16000, input=True, frames_per_buffer=8192)
        self.__stream.start_stream()

        listening = True
        looking_for_commands = False

        while True:
            if listening:
                data = self.__stream.read(4096, exception_on_overflow=False)
                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.Result()
                    res = text[14:-3]
                    if len(res):
                        if (commands):
                            if res == 'start listening':
                                looking_for_commands = True
                                listening = False
                                sleep(1)
                                self.speak.speak_system('startup', True)
                                sleep(2)
                                listening = True
                            elif res == 'stop listening':
                                self.speak.speak_system('startup', False)
                                looking_for_commands = False
                            elif looking_for_commands:
                                print('')
                            # execute_app(res)
                        # execute_app(res)
                        else:
                            print(res)

    def listen(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.__model = Model(
            r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")
        self.__recognizer = KaldiRecognizer(self.__model, 16000)
        self.mic = pyaudio.PyAudio()
        self.__stream = self.mic.open(format=pyaudio.paInt16, channels=1,
                                      rate=16000, input=True, frames_per_buffer=8192)
        self.__stream.start_stream()
        listening = True
        print('listen funciton')
        while True:
            if listening:
                data = self.__stream.read(4096, exception_on_overflow=False)
                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.Result()
                    res = text[14:-3]
                    if len(res):
                        listening = False
                        sleep(1)
                        print(res)
                        return res

    def listen_write(self):
        self.__stream.start_stream()
        listening = True
        print('listen funciton write')
        while True:
            if listening:
                data = self.__stream.read(4096, exception_on_overflow=False)
                if self.__recognizer.AcceptWaveform(data):
                    text = self.__recognizer.PartialResult()
                    res = text
                    if len(res):
                        listening = False
                        sleep(1)
                        print(res)
                        yield res