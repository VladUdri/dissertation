from commands.command import ICommand
from speak import Speak


class GoogleWikipediaSearch(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            # speaker.speak('search', self.app, True)
            self.app.google_wikipedia_search()
        except:
            # speaker.speak('search', self.app, None)
            print('exception GoogleWikipediaSearch')
        # else:
            # speaker.speak('search', self.app, False)
