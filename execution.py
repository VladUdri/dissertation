from word import Word
from time import sleep
from commands import Commands
import pyautogui as pg
from nltk.tokenize import sent_tokenize, word_tokenize
from utils import move_and_click
from computer_actions import ComputerActions
from outlook import Outlook

status = []


def verify_translation_execute(text):
    comm = Commands(text)
    res = comm.checker()
    print(res)
    if res == '{new_word}':
        word = Word('word')
        print('Opening a new word document. Please wait...')
        word.open_app()
        sleep(1)
        create = word.create_blank_docx()
        sleep(2)
        if create:
            print('Word document successfully created!')
            status.append('word_opened')
            status.append('in_word')
        return res
    elif res == '{taskbar_word}':
        if pg.locateCenterOnScreen('img\\open_word.png') is not None:
            move_and_click('img\\open_word.png')
            status.append('in_word')

    elif res == '{save_word}' and 'in_word' in status:
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
    elif res == '{new_outlook}':
        outlook = Outlook('Outlook')
        outlook.open_app()
        sleep(1)
        return res
    elif res == '{taskbar_outlook}':
        outlook = Outlook('Outlook')
        outlook.open_taskbar()
        sleep(1)
        return res
    elif res == '{volume_up}':
        volume = ComputerActions()
        volume.volume_up()
        sleep(0.5)
    elif res == '{volume_down}':
        volume = ComputerActions()
        volume.volume_down()
        sleep(0.5)
    elif res == '{brightness_up}':
        volume = ComputerActions()
        volume.brightness_up()
        sleep(0.5)
    elif res == '{brightness_down}':
        volume = ComputerActions()
        volume.brightness_down()
        sleep(0.5)
    elif res == '{new_email}':
        outlook = Outlook('Outlook')
        if pg.locateCenterOnScreen('img\\in_outlook.png', confidence=0.8) is not None:
            outlook.send_email()
            sleep(1)
        else:
            if pg.locateCenterOnScreen('img\\taskbar_outlook.png',
                                       confidence=0.8) is not None or pg.locateCenterOnScreen(
                'img\\taskbar_outlook_empty.png'):
                outlook.open_taskbar()
                sleep(1)
                outlook.send_email()
                sleep(1)
            else:
                outlook.open_app()
                sleep(1)
                outlook.send_email()
                sleep(1)
    elif res == '{write}':
        write_text()
    elif res == '{edit_word}':
        text_to_edit = pg.prompt('Text to edit')
        new_text = pg.prompt('New text')
        print(text_to_edit)
        print(new_text)
        word = Word('word')
        word.find_edit_words(text_to_edit, new_text, word)

def write_text():
    word = Word('word')
    text = ''
    while text != 'end write':
        text = pg.prompt(text='Text', title='Write text', default='')
        if text == 'end write':
            break
        comm = Commands(text)
        res = comm.execute(word, False)
        # return res
