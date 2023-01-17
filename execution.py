from word import Word
from time import sleep
from commands import Commands
import pyautogui as pg
from nltk.tokenize import sent_tokenize, word_tokenize

status = []


def verify_translation_execute(text):
    comm = Commands(text)
    res = comm.checker()
    if res == '{new_word}':
        word = Word('word')
        print('Opening a new word document. Please wait...')
        word.open_app()
        sleep(1)
        create = word.create_blank_docx()
        sleep(2)
        if create:
            print('Word document successfully created!')
            status.append('word')
        return res
    elif res == '{save_word}' and 'word' in status:
        if status[-1] != 'word_saved':
            word = Word('word')
            doc_name = pg.prompt(text='Provide a name for the document', title='Name for document', default='')
            sleep(1)
            word.save(doc_name)
            sleep(2)
            status.append('word_saved')
        else:
            print('Document already saved! Add modifications to save it again.')
        return res
    elif res == '{write}':
        sleep(1)
        write_text()
        sleep(2)
        status.append('write')



def write_text():
    word = Word('word')
    text = ''
    while True and text != None:
        text = pg.prompt(text='Text', title='Write text', default='')
        comm = Commands(text)
        comm.execute(word, False)