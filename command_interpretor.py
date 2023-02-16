from commands.open import Open
from commands.close import Close
from commands.new_word import NewWord
from commands.new_notepad import NewNotepad
from commands.send_email import SendEmail
from commands.save import Save
from commands.vosk_dictation import VoskDictation
from commands.brightness import Brightness
from commands.volume import Volume


class CommandInterpretor:
    def __init__(self, app) -> None:
        self.app = app
        self.commands = {
            'open_app': Open(self.app),
            'close_app': Close(self.app),
            'create_new_word': NewWord(self.app),
            'save_as_word': Save(self.app),
            'start_dictation': VoskDictation(),
            'create_new_notepad': NewNotepad(self.app),
            'save_as_notepad': Save(self.app),
            'send_email': SendEmail(self.app),
            'brightness_up': Brightness(self.app, 'up'),
            'brightness_down': Brightness(self.app, 'down'),
            'brightness_value': Brightness(self.app, 'value'),
            'volume_up': Volume(self.app, 'up'),
            'volume_down': Volume(self.app, 'down'),
            'volume_value': Volume(self.app, 'value'),
        }

    def process_command(self, command):
        if command in self.commands:
            self.commands[command].execute()
        else:
            print('not known')
