from commands.command import ICommand
from speak import Speak


class Close(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('close_app', True)
            self.app.close_app()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('close_app', False)
