from commands.command import ICommand
from speak import Speak


class OutlookEmailCreateNew(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('event_add_title', self.app, True)
            # if self.app._state == 'open':
            self.app.create_new()
        except:
            # speaker.speak('create_event', self.app, None)
            print('exception OutlookEmailCreateNew')
        # else:
        #     speaker.speak('create_event', self.app, False)
