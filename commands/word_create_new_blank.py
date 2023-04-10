from commands.command import ICommand
from speak import Speak


class WordCreateNewBlank(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('create_new', self.app, True)
            self.app.word_create_new_blank()
        except:
            # speaker.speak('create_new', self.app, None)
            print('exception create new')
        # else:
        #     speaker.speak('create_new', self.app, False)
