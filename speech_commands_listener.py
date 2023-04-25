# Import necessary libraries and modules
import pytesseract
import json
import sys
import queue
import sounddevice as sd
import vosk
from speak import Speak
from voice_interpreter import VoiceInterpreter

# Set Vosk log level to suppress log messages
vosk.SetLogLevel(-1)

# Define a class for listening for voice commands
class SpeechCommandListener():

    # Initialize class with the stop and trigger commands
    def __init__(self, stop_command='close application', trigger_command='initialize application'):
        # Create a queue to store audio data
        self.q = queue.Queue()
        # Initialize variables for stop and trigger commands
        self.previous_line = ""
        self.stop_command = stop_command
        self.trigger_command = trigger_command
        # Initialize a Speak object for text-to-speech output
        self.speaker = Speak()

    # Method for listening for voice commands
    def listen_for_commands(self, REC, SAMPLERATE, one_time=False):
        # Speak a prompt asking the user to say the trigger command to start the program
        self.speaker.simple_speak('To start the program say initialise application')

        try:
            # Use sounddevice to capture audio data
            with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=8000, device=None, dtype='int16', channels=1,
                                   callback=self._callback):
                # Initialize variables for processing audio data
                fin = new_fin = ''
                listening = True
                waiting_for_commands = False

                while True:
                    # If listening flag is True, process the audio data
                    if listening == True:
                        # Get audio data from the queue
                        data = self.q.get()
                        # Pass audio data to Vosk speech recognizer and get the result
                        if REC.AcceptWaveform(data):
                            d = json.loads(REC.Result())
                        else:
                            d = json.loads(REC.PartialResult())
                        # Process the result for each key in the dictionary
                        for key in d.keys():
                            if d[key]:
                                if d[key] != self.previous_line or key == 'text':
                                    if "text" in d:
                                        fin = new_fin
                                        new_fin = d["text"]
                                    else:
                                        fin = new_fin
                                        new_fin = d["partial"]
                                    # If the stop command is detected, exit the program
                                    if d[key] == self.stop_command:
                                        with open('last_app/last_app.txt', 'w') as h:
                                            h.write('')
                                        self.speaker.simple_speak('Good bye!')
                                        return
                                    # If the trigger command is detected, start listening for commands
                                    elif d[key] == self.trigger_command and waiting_for_commands == False:
                                        self.speaker.simple_speak('Welcome!')
                                        waiting_for_commands = True
                                        self.q.queue.clear()

                                    # Print the detected command to the console
                                    print('Detected command: ' + d[key])
                                    self.previous_line = d[key]
                    # If waiting_for_commands flag is True, listen for specific commands
                    if waiting_for_commands == True:
                        if fin == new_fin and fin != '' and new_fin != '' and fin != self.trigger_command:
                            try:
                                listening = False
                                # Pass the command to a VoiceInterpreter object to execute
                                res = VoiceInterpreter().execute(fin)
                            except:
                                print('except')
                            else:
                                # Clear the queue to prevent leftover audio data
                                self.q.queue.clear()
                                
                                # If the command result is None, listening should resume
                                if res is None:
                                    listening = True
                                
                                # If 'one_time' mode is on, return the command result and exit the loop
                                if one_time == True:
                                    return fin
                                
                                # Reset 'fin' and 'new_fin' to prepare for the next command
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
