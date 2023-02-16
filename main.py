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
from outlook import Outlook
from computer_actions import ComputerActions
if __name__ == '__main__':
    w = Word('word', 'new_created')
    n = Notepad('notepad', 'closed')
    o = Outlook()
    # Speak().simple_speak('hello')
    # CommandInterpretor(w).process_command("open_app")
    # CommandInterpretor(w).process_command("create_new_word")
    # print(o._state)
    c = ComputerActions()
    # CommandInterpretor(c).process_command("brightness_up")
    # time.sleep(2)
    # CommandInterpretor(c).process_command("brightness_down")
    # time.sleep(2)
    CommandInterpretor(o).process_command("create_event")

    # CommandInterpretor(n).process_command("create_new_notepad")
    # time.sleep(2)
    # CommandInterpretor(n).process_command("save_as_notepad")
    # print(o._state)
    # VoskDictation().transcribe()
