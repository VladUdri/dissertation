from commands.open import Open
from commands.close import Close
from commands.new_word import NewWord
from commands.new_notepad import NewNotepad
from commands.save import Save
from commands.vosk_dictation import VoskDictation


class CommandInterpretor:
    def __init__(self, app) -> None:
        self.app = app
        self.commands = {
            'open_app': Open(self.app),
            'close_app': Close(self.app),
            'create_new_word': NewWord(self.app),
            'save_as_word': Save(self.app),
            "start_dictation": VoskDictation(),
            'create_new_notepad': NewNotepad(self.app)}

    def process_command(self, command):
        if command in self.commands:
            self.commands[command].execute()
        else:
            print('not known')
