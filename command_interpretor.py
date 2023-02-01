from commands.open import Open
from commands.close import Close
from commands.new import NewWord
from commands.save import Save


class CommandInterpretor:
    def __init__(self, app) -> None:
        self.app = app
        self.commands = {
            'open_app': Open(self.app),
            'close_app': Close(self.app),
            'create_new_word': NewWord(self.app),
            'save_as_word': Save(self.app)
        }

    def process_command(self, command):
        if command in self.commands:
            self.commands[command].execute()
        else:
            print('not known')
