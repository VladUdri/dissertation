import unittest

from convert_text import ConvertText
from command_interpretor import CommandInterpretor
from voice_interpretor import VoiceInterpretor
import json

with open('jsons/all_commands.json') as f:
    comm = json.load(f)

class TestConvertText(unittest.TestCase):

    def test_1(self):
        data = 'open microsoft word'
        function_result = ConvertText(data).process_text()
        expected_result = ['open', 'microsoft', 'word']
        self.assertEqual(function_result, expected_result)

    def test_2(self):
        data = 'create new word document'
        function_result = ConvertText(data).process_text()
        expected_result = ['create', 'new', 'word', 'document']
        self.assertEqual(function_result, expected_result)

    def test_3(self):
        data = 'start dictating'
        function_result = ConvertText(data).process_text()
        expected_result = ['start', 'dictate']
        self.assertEqual(function_result, expected_result)

    def test_4(self):
        data = 'open microsoft word'
        function_result = ConvertText(data).process_text()
        expected_result = ['open', 'microsoft', 'word']
        self.assertEqual(function_result, expected_result)

    def test_5(self):
        data = 'start writing bold'
        function_result = ConvertText(data).process_text()
        expected_result = ['start', 'write', 'bold']
        self.assertEqual(function_result, expected_result)

    def test_6(self):
        data = 'change the size of the font'
        function_result = ConvertText(data).process_text()
        expected_result = ['change', 'size', 'font']
        self.assertEqual(function_result, expected_result)

    def test_7(self):
        data = 'start writing text'
        function_result = ConvertText(data).process_text()
        expected_result = ['start', 'write', 'text']
        self.assertEqual(function_result, expected_result)

    def test_8(self):
        data = 'add title'
        function_result = ConvertText(data).process_text()
        expected_result = ['add', 'title']
        self.assertEqual(function_result, expected_result)

    def test_9(self):
        data = 'add new shortcuts'
        function_result = ConvertText(data).process_text()
        expected_result = ['add', 'new', 'shortcut']
        self.assertEqual(function_result, expected_result)

    def test_10(self):
        data = 'search on wikipedia'
        function_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia']
        self.assertEqual(function_result, expected_result)

    def test_11(self):
        data = 'search    on  wikipedia'
        function_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia']
        self.assertEqual(function_result, expected_result)

    def test_12(self):
        data = 'search on wikipedia, please'
        function_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia', 'please']
        self.assertEqual(function_result, expected_result)

    def test_13(self):
        data = '...please, open this application!'
        function_result = ConvertText(data).process_text()
        expected_result = ['please', 'open', 'application']
        self.assertEqual(function_result, expected_result)

    def test_14_all_stopwords(self):
        data = 'The of and to in a that is for on with it but by at'
        function_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(function_result, expected_result)

    def test_15_empty(self):
        data = ''
        function_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(function_result, expected_result)

    def test_16_whitespaces(self):
        data = '            '
        function_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(function_result, expected_result)

    def test_17(self):
        data = 'She has a cat and a dog as pets'
        function_result = ConvertText(data).process_text()
        expected_result = ['cat', 'dog', 'pet']
        self.assertEqual(function_result, expected_result)

    def test_18(self):
        data = 'The birds are singing and the children are running.'
        function_result = ConvertText(data).process_text()
        expected_result = ['bird', 'sing', 'child', 'run']
        self.assertEqual(function_result, expected_result)

    def test_19(self):
        data = 'The dogs are barking loudly outside the house'
        function_result = ConvertText(data).process_text()
        expected_result = ['dog', 'bark', 'loudly', 'outside', 'house']
        self.assertEqual(function_result, expected_result)

    def test_20(self):
        data = 'The quick brown fox jumps over the lazy dog'
        function_result = ConvertText(data).process_text()
        expected_result = ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog']
        self.assertEqual(function_result, expected_result)


#############################
#### command interpretor ####
#############################


class TestCommandInterpretor(unittest.TestCase):

    def test_1(self):
        s_app = 'word'
        app = 'word'
        last_app = 'word'
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        expected_result = 'word'
        self.assertEqual(function_result, expected_result)

    def test_2(self):
        s_app = 'word'
        app = None
        last_app = 'outlook'
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        expected_result = 'outlook'
        self.assertEqual(function_result, expected_result)

    def test_3(self):
        s_app = 'word'
        app = None
        last_app = ''
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        self.assertIsNone(function_result)

    def test_4(self):
        s_app = 'word'
        app = 'notepad'
        last_app = 'word'
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        expected_result = 'notepad'
        self.assertEqual(function_result, expected_result)

    def test_5(self):
        s_app = 'word'
        app = 'notepad'
        last_app = ''
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        expected_result = 'notepad'
        self.assertEqual(function_result, expected_result)

    def test_6(self):
        s_app = 'word'
        app = 'excel'
        last_app = ''
        aux = CommandInterpretor(s_app, last_app)
        function_result = aux.startup_app(app, last_app)
        expected_result = 'excel'
        self.assertEqual(function_result, expected_result)


#############################
#### voice interpretor ####
#############################


class TestVoiceInterpretor(unittest.TestCase):

    def test_1(self):
        text = 'open word'
        function_result = VoiceInterpretor(comm).get_app(text)
        expected_result = 'word'
        self.assertEqual(function_result, expected_result)

    def test_2(self):
        text = 'create new word document'
        function_result = VoiceInterpretor(comm).get_app(text)
        expected_result = 'word'
        self.assertEqual(function_result, expected_result)

    def test_3(self):
        text = 'send outlook email'
        function_result = VoiceInterpretor(comm).get_app(text)
        expected_result = 'outlook'
        self.assertEqual(function_result, expected_result)

    def test_4(self):
        text = 'computer increase brightness'
        function_result = VoiceInterpretor(comm).get_app(text)
        expected_result = 'computer'
        self.assertEqual(function_result, expected_result)

    def test_5(self):
        text = 'search on google'
        function_result = VoiceInterpretor(comm).get_app(text)
        expected_result = 'google'
        self.assertEqual(function_result, expected_result)

    def test_6(self):
        with open('jsons/last_app/last_app.txt', 'w') as h:
            h.write('')
        text = 'search on reddit'
        function_result = VoiceInterpretor(comm).get_app(text)
        self.assertIsNone(function_result)

#########################################################
    def test_7(self):
        text = 'search on google'
        app = 'google'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'google_search'
        self.assertEqual(function_result, expected_result)

    def test_8(self):
        text = 'search on internet'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        self.assertIsNone(function_result)

    def test_9(self):
        text = 'search on wikipedia'
        app = 'google'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'google_wikipedia_search'
        self.assertEqual(function_result, expected_result)

    def test_10(self):
        text = 'i want to send an email'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'outlook_email_send'
        self.assertEqual(function_result, expected_result)

    def test_11(self):
        text = 'add the destination email'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'outlook_email_add_to'
        self.assertEqual(function_result, expected_result)

    def test_12(self):
        text = 'add the destination email'
        app = 'notepad'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        self.assertIsNone(function_result)

    def test_13(self):
        text = 'open outlook'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'open_app'
        self.assertEqual(function_result, expected_result)

    def test_14(self):
        text = 'close outlook'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'close_app'
        self.assertEqual(function_result, expected_result)

    def test_15(self):
        text = 'i need to create a new word document'
        app = 'word'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'word_create_new'
        self.assertEqual(function_result, expected_result)

    def test_16(self):
        text = 'create new blank'
        app = 'word'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'word_create_new_blank'
        self.assertEqual(function_result, expected_result)

    def test_17(self):
        text = 'create new blank document'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        self.assertIsNone(function_result)

    def test_18(self):
        text = 'start writing'
        app = 'word'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'start_dictation'
        self.assertEqual(function_result, expected_result)

    def test_19(self):
        text = 'start writing'
        app = 'notepad'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'start_dictation'
        self.assertEqual(function_result, expected_result)

    def test_20(self):
        text = 'increase brightness'
        app = 'computer'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'computer_brightness_up'
        self.assertEqual(function_result, expected_result)

    def test_21(self):
        text = 'change brightness'
        app = 'computer'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'computer_brightness_value'
        self.assertEqual(function_result, expected_result)

    def test_22(self):
        text = 'add new event to calendar'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'outlook_event_create'
        self.assertEqual(function_result, expected_result)

    def test_23(self):
        text = 'add start time'
        app = 'outlook'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        expected_result = 'outlook_event_add_start_time'
        self.assertEqual(function_result, expected_result)

    def test_24(self):
        text = 'add start time'
        app = 'computer'
        function_result = VoiceInterpretor(comm).search_str(text, app)
        self.assertIsNone(function_result)


if __name__ == '__main__':
    unittest.main()
