from commands.command import ICommand
from speak import Speak


class NotepadCreateNew(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('notepad_create_new', True)
            self.app.notepad_create_new()
        except:
            speaker.simple_speak('Something went wrong, please try again!')

        else:
            speaker.speak('notepad_create_new', False)

