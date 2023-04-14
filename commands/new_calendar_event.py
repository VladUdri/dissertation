from commands.command import ICommand
from speak import Speak


class NewEvent(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_create_event', self.app, True)
            # if self.app._state == 'open':
            self.app.outlook_create_event()
        except:
            speaker.speak('outlook_create_event', self.app, None)
            print('exception outlook_create_event')
        # else:
        #     speaker.speak('outlook_create_event', self.app, False)
