from commands.command import ICommand


class Close(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app
        # self.voice = voice

    def execute(self):
        try:
            # speak()
            if self.app._state != 'closed':
                self.app.close_app()
            # setstate
            # speak()
        except:
            print('exception open')
