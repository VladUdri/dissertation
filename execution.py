from time import sleep
from convert_text import ConvertText
from word import Word
from outlook import Outlook
import json
from application import Applicationss
from utils import speak
from random import randint

default_apps = {'word': ['open_app', 'close_app', 'create_new'],
                'outlook': ['open_app', 'close_app', 'create_new']}

start_apps = {}


def default_actions(obj, action, app, engine):
    speak(engine, decode_speech_feedback(action, app, start=True))
    match action:
        case 'open_app':
            res = obj.open_app()
        case 'close_app':
            res = obj.close_app()
        case 'create_new':
            if app == 'word':
                res = obj.word_create_new()
            elif app == 'outlook':
                res = obj.create_new()
    sleep(1)
    if res:
        speak(engine, decode_speech_feedback(action, app, start=False))


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


def decode_speech_feedback(action, last_app, start):
    # comm = get_json()
    with open('all_commands.json') as f:
        comm = json.load(f)
    if start == True:
        index = randint(0, len(comm[action]['start_responses']) - 1)
        return comm[action]['start_responses'][index].replace('<app_name>', last_app)
    else:
        index = randint(0, len(comm[action]['stop_responses']) - 1)
        return comm[action]['stop_responses'][index].replace('<app_name>', last_app)


def startup_app(app):
    match app:
        case 'word':
            if 'word' not in start_apps:
                start_apps['word'] = Word('word', 'closed')
        case 'outlook':
            if 'outlook' not in start_apps:
                start_apps['outlook'] = Outlook('outlook', 'closed')


def execute_app(app, action, engine):
    if action not in default_apps[app]:
        return False
    default_actions(start_apps[app], action, app, engine)


def execute(phrase, engine, last_app):
    convertion = ConvertText(phrase)
    converted_text = convertion.process_text()
    text_to_compare = ' '.join(converted_text[0:len(converted_text)])
    print(text_to_compare)
    action = search_str(text_to_compare)
    if action is not None:
        app = get_app(text_to_compare)
        if app is not None:
            last_app = app
        else:
            if last_app != '':
                app = last_app
            else:
                # todo maybe something else
                speak(engine=engine,
                      text='Please say the command again, but specify the app!')
                return
    else:
        speak(engine=engine, text='Sorry! I don\'t know that.')
        return
    startup_app(app)
    res = execute_app(app=app, action=action, engine=engine)
    if res == False:
        speak('Action not available for this app.')
        return
    return last_app


# idee: creeaza niste states pt fiecare obiect. de exemplu. am deschis un word, dar nu am creeat un doc nou => status opened; am deschis un word si am creat un doc nou => status created. in asa fel
