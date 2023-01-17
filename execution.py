from word import Word
from time import sleep
from commands import Commands
from utils import move_and_click
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def verify_translation_execute(text):
    comm = Commands(text)
    res = comm.translate_for_word(text)
    if res == '{new_word}':
        word = Word('word')
        print('Opening a new word document. Please wait...')
        word.open_app()
        sleep(1)
        create = word.create_blank_docx()
        sleep(2)
        if create:
            print('Word document successfully created!')
        return res
