from vosk_voice import VoskModel
from word import Word
from time import sleep
from commands import Commands
import nltk
from convert_text import ConvertText
import pyttsx3 as pt
import execution

if __name__ == '__main__':
    # word = Word('word')
    # sleep(3)
    # # word.convert_text()
    # comm = Commands('asd')
    # text = 'Seen from a boat, approaching align left the paragraph island through cold, choppy, white-flecked seas, the island of Staffa looks bold like a dense grey forest bold of rock align off the right western italic coast of Scotland. title Columns title align justify  of basalt push up and then flower out into a puffy, cloud-like summit paragraph on top of which the plant life of the island grows, a rolling plain of grass and heather and machair whipped by the sea-wind. Underlined italic The island is made of very ancient rock, but is so strange-looking and so dynamic that you have to tell yourself, repeatedly, that it has been here for a long, long time, such a long time that the best guesses of humankind as to its age can only approximate a range of years that could encompass, with ease, every meaningful incident of human civilisation.'
    # comm.write_text_new(text)
    # vos = VoskModel()
    # vos.test()

    # test = ConvertText('Start writing in word')
    # text.
    # test.process_text ()
    # vos = VoskModel()
    # while True:
    #     res = vos.test()
    #     if res is not None and res is not '':
    #         print(res)

    engine = pt.init()
    engine.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    execution.execute_app('Create a new word document', engine)
