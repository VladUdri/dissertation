from command import ICommand
from speak import Speak


class SendEmail(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('send_email', self.app, True)
            if self.app._state == 'open':
                self.app.send_email()
        except:
            speaker.speak('send_email', self.app, None)
            print('exception send email')
        else:
            speaker.speak('send_email', self.app, False)
