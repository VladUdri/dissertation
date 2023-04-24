from commands.command import ICommand
from speak import Speak


class OutlookEmailCreateNew(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('outlook_email_create_new', True)
            self.app.outlook_email_create_new()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('outlook_email_create_new', False)
