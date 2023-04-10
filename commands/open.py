from commands.command import ICommand
from speak import Speak


class Open(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        print('!!!!!!!!!!!!!!!!')
        speaker = Speak()
        try:
            # speaker.speak('open_app', self.app, True)
            self.app.open_app()
        except:
            speaker.speak('open_app', self.app, None)
            print('exception open')
        # else:
            # speaker.speak('open_app', self.app, False)
