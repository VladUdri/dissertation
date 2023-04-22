from application import IApplications
from one_answer_listener import OneAnswerListener
import webbrowser


class Google(IApplications):
    def __init__(self, app_name='google'):
        super().__init__(app_name)

    def google_search(self):
        url = 'https://www.google.com/search?q='
        self.speak.simple_speak('Please wait!')
        res = OneAnswerListener('What do you want to search?').listen_for_commands(True)
        url += res
        webbrowser.get().open(url)

    def google_wikipedia_search(self):
        url = 'https://en.wikipedia.org/wiki/'
        self.speak.simple_speak('Please wait!')
        res = OneAnswerListener(
            'What do you want to search on Wikipedia?').listen_for_commands(True)
        url += res
        webbrowser.get().open(url)
