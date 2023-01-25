import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
import pytesseract
# from execution import execute_app
import pyttsx3 as pt
from time import sleep
import sounddevice as sd
from execution import execute_app


class VoskModel:
    def test(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        engine = pt.init()
        engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

        model = Model(
            r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")

        recognizer = KaldiRecognizer(model, 16000)
        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16, channels=1,
                          rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()

        listening = True
        looking_for_commands = False

        while True:
            if listening:
                data = stream.read(4096, exception_on_overflow=False)
                if recognizer.AcceptWaveform(data):
                    text = recognizer.Result()
                    if len(text[14:-3]):
                        print('#'*50)
                        print(text[14:-3])
                        if text[14:-3] == 'start listening':
                            looking_for_commands = True
                            listening = False
                            sleep(1)
                            engine.say(
                                'How can I help you?')
                            engine.runAndWait()
                            sleep(2)
                            listening = True
                        elif text[14:-3] == 'stop listening':
                            engine.say('Bye, see you!')
                            engine.runAndWait()
                            looking_for_commands = False
                        elif looking_for_commands:
                            execute_app(text[14:-3], engine)
                        # execute_app(text[14:-3])
