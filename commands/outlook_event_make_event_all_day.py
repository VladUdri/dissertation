from commands.command import ICommand
from speak import Speak


class OutlookEventMakeEventAllDay(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_event_make_event_all_day', True)
            self.app.outlook_event_make_event_all_day()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('outlook_event_make_event_all_day', False)
