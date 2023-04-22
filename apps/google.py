from application import IApplications
from one_answer_listener import Voicev
import webbrowser


class Google(IApplications):
    def __init__(self, app_name='google'):
        super().__init__(app_name)

    def create_new(self):
        pass

    def google_search(self):
        url = 'https://www.google.com/search?q='
        self.speak.simple_speak('Please wait!')
        res = Voicev('What do you want to search?').listen_for_commands(True)
        url += res
        webbrowser.get().open(url)

    def google_wikipedia_search(self):
        url = 'https://en.wikipedia.org/wiki/'
        self.speak.simple_speak('Please wait!')
        res = Voicev(
            'What do you want to search on Wikipedia?').listen_for_commands(True)
        url += res
        webbrowser.get().open(url)
