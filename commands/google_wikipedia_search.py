from commands.command import ICommand
from speak import Speak


class GoogleWikipediaSearch(ICommand):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app

    def execute(self):
        speaker = Speak()
        try:
            speaker.speak('google_wikipedia_search', True)
            self.app.google_wikipedia_search()
        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            speaker.speak('google_wikipedia_search', False)
