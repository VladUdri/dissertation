from commands.command import ICommand
from speak import Speak


class OutlookEventMakeEventAllDay(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('event_add_title', self.app, True)
            # if self.app._state == 'open':
            self.app.event_make_event_all_day()
        except:
            # speaker.speak('create_event', self.app, None)
            print('exception OutlookEventMakeEventAllDay')
        # else:
        #     speaker.speak('create_event', self.app, False)
