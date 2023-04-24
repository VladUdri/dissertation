from application import IApplications
from one_answer_listener import OneAnswerListener
import webbrowser


class Google(IApplications):
    def __init__(self, app_name='google'):
        super().__init__(app_name)  

    def google_search(self):
        # Set the base url for Google search
        url = 'https://www.google.com/search?q='  
        self.speak.simple_speak('Please wait!')  
        # Ask the user for the search query and listen for the response
        res = OneAnswerListener('What do you want to search?').listen_for_commands(True)
        # Append the user's response to the url
        url += res  
        # Open the url in the default web browser
        webbrowser.get().open(url)

    def google_wikipedia_search(self):
        # Set the base url for Wikipedia search
        url = 'https://en.wikipedia.org/wiki/'  
        self.speak.simple_speak('Please wait!')
        # Ask the user for the search query and listen for the response
        res = OneAnswerListener(
            'What do you want to search on Wikipedia?').listen_for_commands(True)          
        # Append the user's response to the url
        url += res  
        # Open the url in the default web browser
        webbrowser.get().open(url) 

