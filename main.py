from word import Word
import pyttsx3 as pt
import pyautogui as pg
import pygetwindow as gw
from time import sleep
from key_action import KeyAction
import win32com.client
from commands.open import Open
from commands.close import Close
from speak import Speak
from command_interpretor import CommandInterpretor

if __name__ == '__main__':
    w = Word('word', 'closed')
    # Speak().execute('hello')
    CommandInterpretor(w).process_command("open_app")
    CommandInterpretor(w).process_command("create_new_word")
    CommandInterpretor(w).process_command("save_as_word")
    # print(w._app_name)