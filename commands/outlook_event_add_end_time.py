from commands.command import ICommand
from speak import Speak


class OutlookEventAddEndTime(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_event_add_end_time', True)
            self.app.outlook_event_add_end_time()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('outlook_event_add_end_time', False)
