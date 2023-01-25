import pyaudio
from vosk import Model, KaldiRecognizer
import pytesseract

class VoskModel:
    def test(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        model = Model(r"D:\\pythonProject1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph")
        
        recognizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()

        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                print(text)
                # print(text[14:-3])
