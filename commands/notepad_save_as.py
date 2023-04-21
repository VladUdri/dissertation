from commands.command import ICommand
from speak import Speak


class NotepadSaveAs(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('notepad_save_as', True)
            self.app.notepad_save_as()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('notepad_save_as', False)
