from commands.command import ICommand
from speak import Speak


class OutlookEventAddEndTime(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('event_add_title', self.app, True)
            # if self.app._state == 'open':
            self.app.event_add_end_time()
        except:
            # speaker.speak('outlook_create_event', self.app, None)
            print('exception OutlookEventAddEndTime')
        # else:
        #     speaker.speak('outlook_create_event', self.app, False)
