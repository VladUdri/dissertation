from word import Word
from command_interpretor import CommandInterpretor
import pyautogui as pg
import time
from key_action import KeyAction
from write_text import WriteText
# from vost_text import VoskModell
from commands.vosk_dictation import VoskDictation
from word2number import w2n
from speak import Speak
from notepad import Notepad

if __name__ == '__main__':
    w = Word('word', 'new_created')
    n = Notepad('notepad', 'closed')
    # Speak().simple_speak('hello')
    # CommandInterpretor(w).process_command("open_app")
    # CommandInterpretor(w).process_command("create_new_word")
    CommandInterpretor(n).process_command("open_app")
    CommandInterpretor(n).process_command("create_new_notepad")
    print(n._state)
    # VoskDictation().transcribe()
