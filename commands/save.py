from command import ICommand
from speak import Speak


class Save(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('save_as', self.app, True)
            if self.app._state == 'new_created':
                self.app.save_as()
        except:
            speaker.speak('save_as', self.app, None)
            print('exception create new')
        else:
            speaker.speak('save_as', self.app, False)
