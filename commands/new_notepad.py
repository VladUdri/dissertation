from commands.command import ICommand
from speak import Speak


class NewNotepad(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('create_new', self.app, True)
            # if self.app._state == 'open':
            self.app.create_new()
        except:
            speaker.speak('create_new', self.app, None)
            print('exception create new')
        # else:
            # speaker.speak('create_new', self.app, False)
