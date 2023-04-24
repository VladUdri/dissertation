from commands.command import ICommand
from speak import Speak


class Open(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('open_app', True)
            self.app.open_app()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('open_app', False)
