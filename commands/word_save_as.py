from commands.command import ICommand
from speak import Speak


class Save(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('word_save_as', True)
            self.app.word_save_as()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('word_save_as', False)