from time import sleep
from convert_text import ConvertText
from final_word import Word
from outlook import Outlook
import json
from final_applications import Applicationss

default_apps = {'word': ['open_app', 'close_app'],
                'outlook': ['open_app', 'close_app']}

start_apps = {}


def get_json():
    with open('all_commands.json') as f:
        comm = json.load(f)
    return comm['default_commands']


def get_app(text):
    for word in text.split(' '):
        if word in default_apps:
            return word
    return None


def search_str(text):
    comm = get_json()
    for key in comm:
        for i in range(0, len(comm[key]['patterns'])):
            if all(substring in text.lower() for substring in comm[key]['patterns'][i]):
                return key
    return None


def startup_app(app):
    match app:
        case 'word':
            if 'word' not in start_apps:
                start_apps['word'] = Word('word', 'closed')
        case 'outlook':
            if 'outlook' not in start_apps:
                start_apps['outlook'] = Outlook('outlook', 'closed')


def execute_app(phrase, engine):
    convertion = ConvertText(phrase)
    converted_text = convertion.process_text()
    text_to_compare = ' '.join(converted_text[0:len(converted_text)])
    # print(text_to_compare)
    action = search_str(text_to_compare)
    if action is not None:
        app = get_app(text_to_compare)
    else:
        app = ''
    startup_app(app)
    start_apps[app].open_app()


# idee: creeaza niste states pt fiecare obiect. de exemplu. am deschis un word, dar nu am creeat un doc nou => status opened; am deschis un word si am creat un doc nou => status created. in asa fel
