from AppOpener import open, mklist, give_appnames
from word import Word
from time import sleep
from commands import Commands
from nltk.tokenize import sent_tokenize, word_tokenize
import pyautogui as pg

if __name__ == '__main__':

    word = Word('word')
    sleep(3)
    # word.convert_text()
    comm = Commands('asd')
    text = 'Seen from a boat, approaching align left the paragraph island through cold, choppy, white-flecked seas, the island of Staffa looks bold like a dense grey forest bold of rock align off the right western italic coast of Scotland. title Columns title align justify  of basalt push up and then flower out into a puffy, cloud-like summit paragraph on top of which the plant life of the island grows, a rolling plain of grass and heather and machair whipped by the sea-wind. Underlined italic The island is made of very ancient rock, but is so strange-looking and so dynamic that you have to tell yourself, repeatedly, that it has been here for a long, long time, such a long time that the best guesses of humankind as to its age can only approximate a range of years that could encompass, with ease, every meaningful incident of human civilisation.'
    comm.write_text_new(text)
