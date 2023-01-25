from time import sleep
from convert_text import ConvertText
from word import Word
from outlook import Outlook
status = []


# def verify_translation_execute(text):
#     comm = Commands(text)
#     res = comm.checker()
#     print(res)
#     if res == '{new_word}':
#         word = Word('word')
#         print('Opening a new word document. Please wait...')
#         word.open_app()
#         sleep(1)
#         create = word.create_blank_docx()
#         sleep(2)
#         if create:
#             print('Word document successfully created!')
#             status.append('word_opened')
#             status.append('in_word')
#         return res
#     elif res == '{taskbar_word}':
#         if pg.locateCenterOnScreen('img\\open_word.png') is not None:
#             move_and_click('img\\open_word.png')
#             status.append('in_word')

#     elif res == '{save_word}' and 'in_word' in status:
#         if status[-1] != 'word_saved':
#             word = Word('word')
#             doc_name = pg.prompt(
#                 text='Provide a name for the document', title='Name for document', default='')
#             sleep(1)
#             word.save(doc_name)
#             sleep(2)
#             status.append('word_saved')
#         else:
#             print('Document already saved! Add modifications to save it again.')
#         return res
#     elif res == '{new_outlook}':
#         outlook = Outlook('Outlook')
#         outlook.open_app()
#         sleep(1)
#         return res
#     elif res == '{taskbar_outlook}':
#         outlook = Outlook('Outlook')
#         outlook.open_taskbar()
#         sleep(1)
#         return res
#     elif res == '{volume_up}':
#         volume = ComputerActions()
#         volume.volume_up()
#         sleep(0.5)
#     elif res == '{volume_down}':
#         volume = ComputerActions()
#         volume.volume_down()
#         sleep(0.5)
#     elif res == '{brightness_up}':
#         volume = ComputerActions()
#         volume.brightness_up()
#         sleep(0.5)
#     elif res == '{brightness_down}':
#         volume = ComputerActions()
#         volume.brightness_down()
#         sleep(0.5)
#     elif res == '{new_email}':
#         outlook = Outlook('Outlook')
#         if pg.locateCenterOnScreen('img\\in_outlook.png', confidence=0.8) is not None:
#             outlook.send_email()
#             sleep(1)
#         else:
#             if pg.locateCenterOnScreen('img\\taskbar_outlook.png',
#                                        confidence=0.8) is not None or pg.locateCenterOnScreen(
#                     'img\\taskbar_outlook_empty.png'):
#                 outlook.open_taskbar()
#                 sleep(1)
#                 outlook.send_email()
#                 sleep(1)
#             else:
#                 outlook.open_app()
#                 sleep(1)
#                 outlook.send_email()
#                 sleep(1)
#     elif res == '{write}':
#         write_text()
#     elif res == '{edit_word}':
#         text_to_edit = pg.prompt('Text to edit')
#         new_text = pg.prompt('New text')
#         print(text_to_edit)
#         print(new_text)
#         word = Word('word')
#         word.find_edit_words(text_to_edit, new_text, word)


# def write_text():
#     word = Word('word')
#     text = ''
#     while text != 'end write':
#         text = pg.prompt(text='Text', title='Write text', default='')
#         if text == 'end write':
#             break
#         comm = Commands(text)
#         res = comm.execute(word, False)
#         # return res

voice_init = {'open word': {'start': 'Opening Word.', 'end': 'Word is open'}, 'open outlook': {'start': 'Opening Outlook.', 'end': 'Outlook opened'},
              'start write word': {'start': 'You can start dictating', 'end': 'Dictation stopped'}, 'start write': {'start': 'You can start dictating', 'end': 'Dictation stopped'},
              'new word document': {'start': 'Creating a new Word document.', 'end': 'A new word document is created.'}}
apps = {'word': {'object': '', 'status':''} , 'outlook': ''}


def execute_app(phrase, engine):
    convertion = ConvertText(phrase)
    converted_text = convertion.process_text()
    text_to_compare = ' '.join(converted_text[0:len(converted_text)])
    print(text_to_compare)
    if 'open word' in text_to_compare:
        text_to_compare = 'open word'
        print('Opening word...')
        engine.say(voice_init[text_to_compare]['start'])
        engine.runAndWait()
        apps['word'] = Word('word')
        apps['word'].open_application()
    elif 'open outlook' in text_to_compare:
        text_to_compare = 'open outlook'
        print('Opening outlook...')
        engine.say(voice_init[text_to_compare]['start'])
        engine.runAndWait()
        apps['outlook'] = Outlook('outlook')
        res = apps['outlook'].open_application()
        if res:
            engine.say('voice_init[text_to_compare]')
            engine.runAndWait()
    elif 'new word document' in text_to_compare:
        text_to_compare = 'new word document'
        print('Creating...')
        engine.say(voice_init[text_to_compare]['start'])
        engine.runAndWait()
        if apps['word'] is '':
            apps['word'] = Word('word')
        first_res = apps['word'].open_application()
        res = apps['word'].create_new_doc()
        if first_res is True and res is True:
            engine.say(voice_init[text_to_compare]['end'])
            engine.runAndWait()
    elif 'start write word' in text_to_compare:
        engine.say(voice_init[text_to_compare])
        engine.runAndWait()

#idee: creeaza niste states pt fiecare obiect. de exemplu. am deschis un word, dar nu am creeat un doc nou => status opened; am deschis un word si am creat un doc nou => status created. in asa fel