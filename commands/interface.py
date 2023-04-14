from commands.command import ICommand
from speak import Speak
from app_interface import AppInt


class Interface(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('run_interface', True)
            AppInt().run()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        # else:
            speaker.speak('run_interface', False)
