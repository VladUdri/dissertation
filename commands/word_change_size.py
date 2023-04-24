from commands.command import ICommand
from speak import Speak


class WordChangeSize(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('word_change_size', True)
            self.app.word_change_size()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('word_change_size', False)
