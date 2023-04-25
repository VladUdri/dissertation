import json
import sys
import queue
import sounddevice as sd
import vosk
from init_voice import VoiceInit

from speak import Speak

vosk.SetLogLevel(-1)

# Define OneAnswerListener class
class OneAnswerListener():
    def __init__(self, speech='', safety_word='stop listening'):
        # Create queue object
        self.one_q = queue.Queue()

        # Initialize previous line
        self.previous_line = ""
        # Initialize previous length
        self.previous_length = 0
        # Set safety word
        self.safety_word = safety_word
        # Set speech
        self.speech = speech
        # Create Speak object
        self.speaker = Speak()

    # Define function to listen for commands
    def listen_for_commands(self, one_time=False):
        # Import required variables from main module
        # from main import REC, SAMPLERATE
        REC, SAMPLERATE = VoiceInit().setUp()

        # Speak given speech
        self.speaker.simple_speak(self.speech)
        self.one_q.queue.clear()

        try:
            # Set up raw input stream for recording audio
            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self.__callback):
                # Initialize final and new final lines
                fin = new_fin = ''
                # Set listening flag to True
                listening = True
                # Loop indefinitely
                while True:
                    # If still listening
                    if listening == True:
                        # Get audio data from queue
                        data = self.one_q.get()
                        # Pass audio data to Vosk recognizer
                        if REC.AcceptWaveform(data):
                            d = json.loads(REC.Result())
                        else:
                            d = json.loads(REC.PartialResult())
                        # Loop through keys of recognized speech
                        for key in d.keys():
                            if d[key]:
                                # If new line is detected
                                if d[key] != self.previous_line or key == 'text':
                                    # Update final and new final lines
                                    if "text" in d:
                                        fin = new_fin
                                        new_fin = d["text"]
                                    else:
                                        fin = new_fin
                                        new_fin = d["partial"]
                                    # If safety word is detected, return
                                    if d[key] == self.safety_word:
                                        return
                                    # Update previous line
                                    self.previous_line = d[key]
                    # If final and new final lines are equal and not empty
                    if (fin == new_fin and fin != '' and new_fin != ''):
                        # Set listening flag to False
                        listening = False
                        # If one_time flag is True, return final line
                        if one_time == True:
                            return fin
                        # Reset final and new final lines
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
        self.one_q.put(bytes(indata))
