from commands.command import ICommand
from speak import Speak


class OutlookSendEmail(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_send_email', True)
            self.app.outlook_send_email()
        except:
            speaker.simple_speak('Something went wrong, please try again!')

        else:
            speaker.speak('outlook_send_email', False)
