import pyautogui as pg
from time import sleep
from nltk.tokenize import sent_tokenize, word_tokenize


class Commands():
    available_actions = ['write bold', 'end bold', 'write italic', 'end italic', 'write underlined', 'end underlined',
                         'align justify', 'end justify', 'align center', 'end center',
                         'align left', 'end left', 'align right', 'end right', 'add bullets', 'end bullets']
    available_actions_translated = ['{bold}', '{/bold}', '{italic}', '{/italic}', '{underlined}', '{/underlined}',
                                    '{align_justify}', '{/align_justify}',
                                    '{align_center}', '{/align_center}',
                                    '{align_left}', '{/align_left}', '{align_right}', '{/align_right}', '{bullets}',
                                    '{/bullets}']

    comm = {'word': True, 'save': True, 'write': True, 'writing': True}

    def __init__(self, text):
        self.text = text

    def checker(self):
        for word in range(0, len(self.text)):
            print(self.text[word])
            if self.text[word] in self.comm.keys():
                if self.text[word] == 'word':
                    return self.translate_for_word(self.text, word)
                elif self.text[word] == 'save':
                    return self.translate_for_save(self.text, word)
                elif self.text[word] == 'write' or self.text[word] == 'writing':
                    return self.translate_for_write(self.text, word)

    def translate_for_word(self, text, i):
        if text[i - 1] == 'new' or text[i - 1] == 'create' or (
                text[i - 2] == 'new' and text[i - 1] == 'empty') or (
                text[i - 2] == 'create' and text[i - 1] == 'empty') or (
                text[i - 3] == 'create' and text[i - 2] == 'new' and text[i - 1] == 'empty'):
            return '{new_word}'
        return ''

    def translate_for_save(self, text, i):
        if i + 1 < len(text):
            if text[i + 1] == 'word' or text[i + 1] == 'document':
                return '{save_word}'
        return ''

    # start write; start writing; write text; start writing text; write in word; write in document;
    def translate_for_write(self, text, i):
        if text[i - 1] == 'start' or text[i + 1] == 'text' or (
                text[i - 1] == 'start' and text[i + 1] == 'text') or text[i + 2] == 'word' or \
                text[i + 1] == 'document' or text[i + 2] == 'document':
            return '{write}'
        return ''

    def contains_text(self):
        for index in range(0, len(self.available_actions)):
            if self.available_actions[index] in self.text:
                self.text = self.text.replace(self.available_actions[index], self.available_actions_translated[index])

        return self.text

    def compare_text(self, obj, word):
        print(word)
        if '{bold}' in word:
            obj.change_to_bold()
            replaced = word.replace('{bold}', '')
            return replaced
        if '{/bold}' in word:
            obj.change_to_bold()
            replaced = word.replace('{/bold}', '')
            return replaced
        if '{italic}' in word:
            obj.change_to_italic()
            replaced = word.replace('{italic}', '')
            return replaced
        if '{/italic}' in word:
            obj.change_to_italic()
            replaced = word.replace('{/italic}', '')
            return replaced
        if '{underlined}' in word:
            obj.change_to_underlined()
            replaced = word.replace('{underlined}', '')
            return replaced
        if '{/underlined}' in word:
            obj.change_to_underlined()
            replaced = word.replace('{/underlined}', '')
            return replaced
        if '{align_center}' in word:
            pg.press('enter')
            obj.align_center()
            replaced = word.replace('{align_center}', '')
            return replaced
        if '{/align_center}' in word:
            pg.press('enter')
            obj.align_center()
            replaced = word.replace('{/align_center}', '')
            return replaced

        return word

    def execute(self, obj, is_word):
        self.contains_text()
        split_text = self.text.split()
        for word in split_text:
            to_write = self.compare_text(obj, word)
            if is_word:
                to_write.replace(' ', '')
                obj.write_text(to_write)
            else:
                obj.write_text(to_write + ' ')
