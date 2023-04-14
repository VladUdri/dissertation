from commands.command import ICommand
from speak import Speak


class SendEmail(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_send_email', self.app, True)
            if self.app._state == 'open':
                self.app.outlook_send_email()
        except:
            speaker.speak('outlook_send_email', self.app, None)
            print('exception send email')
        else:
            speaker.speak('outlook_send_email', self.app, False)
