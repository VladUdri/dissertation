from commands.command import ICommand
from speak import Speak
from app_interface import AppInt


class Interface(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        # speaker = Speak()
        try:
            # speaker.speak('new_event', self.app, True)
            AppInt().run()
        except:
            # speaker.speak('new_event', self.app, None)
            print('exception new_event')
        # else:
        #     speaker.speak('new_event', self.app, False)
