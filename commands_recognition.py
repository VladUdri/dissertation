import nltk as nk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer


class CommandsRecognition:
    def __init__(self, text):
        self.text = text

    """
    Function that removes stop words from a text
    """

    def remove_stopwords(self, text):
        res = text.translate(str.maketrans('', '', string.punctuation))
        stop_words = set(stopwords.words("english"))
        words = word_tokenize(res)
        filtered = []
        for word in words:
            if word.casefold() not in stop_words:
                filtered.append(word)
        filtered = [word for word in words if word.casefold()
                    not in stop_words]
        print(filtered)
        return filtered

    """
    Function that lemmatizes the words so everytime we will have the form from dictionary of the word
    - takes text as parameter (a text composed of one or more sentences)
    - returns result (a text having the words lemmetized)
    """

    def lemm(self, text):
        words = word_tokenize(text)
        words_prop = nk.pos_tag(words)
        lemmatizer = WordNetLemmatizer()
        result = ''
        for index in range(0, len(words_prop)):
            part = self.part_of_speech(words_prop[index])
            if part is not '':
                res = lemmatizer.lemmatize(words_prop[index][0], pos=part)
            else:
                res = lemmatizer.lemmatize(words_prop[index][0])

            result += res
            result += ' '
        return result

    """
    Funtion that converts the part of speech so that it can be used in the lemmetizer 
    e.g. NN -> n; VBG -> v
    """

    def part_of_speech(self, touple):
        if touple[1][0] == 'N':
            return 'n'
        elif touple[1][0] == 'V':
            return 'v'
        elif touple[1][0] == 'J':
            return 'a'
        elif touple[1][0] == 'R':
            return 'r'
        else:
            return ''

    def process_text(self):
        lemm_text = self.lemm(self.text)
        result = self.remove_stopwords(lemm_text)
        print(result)
