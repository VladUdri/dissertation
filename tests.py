import unittest

from convert_text import ConvertText


class TestSum(unittest.TestCase):

    def test_1(self):
        data = 'open microsoft word'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['open', 'microsoft', 'word']
        self.assertEqual(funtion_result, expected_result)

    def test_2(self):
        data = 'create new word document'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['create', 'new', 'word', 'document']
        self.assertEqual(funtion_result, expected_result)

    def test_3(self):
        data = 'start dictating'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['start', 'dictate']
        self.assertEqual(funtion_result, expected_result)

    def test_4(self):
        data = 'open microsoft word'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['open', 'microsoft', 'word']
        self.assertEqual(funtion_result, expected_result)

    def test_5(self):
        data = 'start writing bold'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['start', 'write', 'bold']
        self.assertEqual(funtion_result, expected_result)

    def test_6(self):
        data = 'change the size of the font'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['change', 'size', 'font']
        self.assertEqual(funtion_result, expected_result)

    def test_7(self):
        data = 'start writing text'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['start', 'write', 'text']
        self.assertEqual(funtion_result, expected_result)

    def test_8(self):
        data = 'add title'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['add', 'title']
        self.assertEqual(funtion_result, expected_result)

    def test_9(self):
        data = 'add new shortcuts'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['add', 'new', 'shortcut']
        self.assertEqual(funtion_result, expected_result)

    def test_10(self):
        data = 'search on wikipedia'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia']
        self.assertEqual(funtion_result, expected_result)

    def test_11(self):
        data = 'search    on  wikipedia'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia']
        self.assertEqual(funtion_result, expected_result)

    def test_12(self):
        data = 'search on wikipedia, please'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['search', 'wikipedia', 'please']
        self.assertEqual(funtion_result, expected_result)

    def test_13(self):
        data = '...please, open this application!'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['please', 'open', 'application']
        self.assertEqual(funtion_result, expected_result)

    def test_14_all_stopwords(self):
        data = 'The of and to in a that is for on with it but by at'
        funtion_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(funtion_result, expected_result)

    def test_15_empty(self):
        data = ''
        funtion_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(funtion_result, expected_result)

    def test_16_whitespaces(self):
        data = '            '
        funtion_result = ConvertText(data).process_text()
        expected_result = []
        self.assertEqual(funtion_result, expected_result)

    def test_17(self):
        data = 'She has a cat and a dog as pets'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['cat', 'dog', 'pet']
        self.assertEqual(funtion_result, expected_result)

    def test_18(self):
        data = 'The birds are singing and the children are running.'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['bird', 'sing', 'child', 'run']
        self.assertEqual(funtion_result, expected_result)

    def test_19(self):
        data = 'The dogs are barking loudly outside the house'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['dog', 'bark', 'loudly', 'outside', 'house']
        self.assertEqual(funtion_result, expected_result)

    def test_20(self):
        data = 'The quick brown fox jumps over the lazy dog'
        funtion_result = ConvertText(data).process_text()
        expected_result = ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog']
        self.assertEqual(funtion_result, expected_result)

    # def test_1(self):
    #         data = 'open microsoft word'
    #         funtion_result = ConvertText(data).process_text()
    #         expected_result = ['open', 'microsoft', 'word']
    #         self.assertEqual(funtion_result, expected_result)

    # def test_1(self):
    #         data = 'open microsoft word'
    #         funtion_result = ConvertText(data).process_text()
    #         expected_result = ['open', 'microsoft', 'word']
    #         self.assertEqual(funtion_result, expected_result)

    # def test_1(self):
    #         data = 'open microsoft word'
    #         funtion_result = ConvertText(data).process_text()
    #         expected_result = ['open', 'microsoft', 'word']
    #         self.assertEqual(funtion_result, expected_result)


if __name__ == '__main__':
    unittest.main()
