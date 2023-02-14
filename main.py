from word import Word
from command_interpretor import CommandInterpretor
import pyautogui as pg
import time
from key_action import KeyAction
from write_text import WriteText
# from vost_text import VoskModell
from vosk_dictation import VoskDictation
from word2number import w2n
from speak import Speak

if __name__ == '__main__':
    # w = Word('word', 'new_created')
    # Speak().simple_speak('hello')
    # CommandInterpretor(w).process_command("open_app")
    # CommandInterpretor(w).process_command("create_new_word")
    # CommandInterpretor(w).process_command("save_as_word")
    # WriteText().run_write()
    # WriteText().run_write()
    # print(w._app_name)
    VoskDictation().transcribe()
    # print(w2n.word_to_num('one '))
