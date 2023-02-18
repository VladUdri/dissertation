from commands.open import Open
from commands.close import Close
from commands.new_word import NewWord
from commands.new_notepad import NewNotepad
from commands.send_email import SendEmail
from commands.save import Save
from commands.vosk_dictation import VoskDictation
from commands.brightness import Brightness
from commands.volume import Volume
from commands.new_calendar_event import NewEvent
from commands.search import Search
from google import Google
from word import Word
from outlook import Outlook
from computer_actions import ComputerActions
from notepad import Notepad


class CommandInterpretor:

    start_apps = {
        'word': Word(),
        'outlook': Outlook(),
        'google': Google(),
        'notepad': Notepad(),
        'computer': ComputerActions()
    }

    def __init__(self, app) -> None:
        self.app = ''
        self.last_app = ''
        self.startup_app(app)
        self.commands = {
            'open_app': Open(self.start_apps[self.app]),
            'close_app': Close(self.start_apps[self.app]),
            'create_new_word': NewWord(self.start_apps[self.app]),
            'save_as_word': Save(self.start_apps[self.app]),
            'start_dictation': VoskDictation(),
            'create_new_notepad': NewNotepad(self.start_apps[self.app]),
            'save_as_notepad': Save(self.start_apps[self.app]),
            'send_email': SendEmail(self.start_apps[self.app]),
            'brightness_up': Brightness(self.start_apps[self.app], 'up'),
            'brightness_down': Brightness(self.start_apps[self.app], 'down'),
            'brightness_value': Brightness(self.start_apps[self.app], 'value'),
            'volume_up': Volume(self.start_apps[self.app], 'up'),
            'volume_down': Volume(self.start_apps[self.app], 'down'),
            'volume_value': Volume(self.start_apps[self.app], 'value'),
            'create_event': NewEvent(self.start_apps[self.app]),
            'search': Search(self.start_apps[self.app])
        }

    def process_command(self, command):
        if command in self.commands:
            self.commands[command].execute()
        else:
            print('not known')

    def startup_app(self, app):
        print(app)
        if app is not None:
            self.last_app = self.app = app
        else:
            if self.last_app != '':
                self.app = self.last_app
