from commands.command import ICommand
from speak import Speak


class OutlookEventAddTitle(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('event_add_title', self.app, True)
            # if self.app._state == 'open':
            self.app.add_title_event()
        except:
            # speaker.speak('create_event', self.app, None)
            print('exception OutlookEventAddTitle')
        # else:
        #     speaker.speak('create_event', self.app, False)
