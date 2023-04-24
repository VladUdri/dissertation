from commands.command import ICommand
from speak import Speak


class OutlookEventAddTitle(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_event_add_title', True)
            self.app.outlook_event_add_title()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('outlook_event_add_title', False)
