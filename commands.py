import pyautogui as pg
from time import sleep


class Commands():
    available_actions = ['write bold', 'end bold', 'write italic', 'end italic', 'write underlined', 'end underlined',
                         'align justify', 'end justify', 'align center', 'end center',
                         'align left', 'end left', 'align right', 'end right', 'add bullets', 'end bullets']
    available_actions_translated = ['{bold}', '{/bold}', '{italic}', '{/italic}', '{underlined}', '{/underlined}',
                                    '{align_justify}', '{/align_justify}',
                                    '{align_center}', '{/align_center}',
                                    '{align_left}', '{/align_left}', '{align_right}', '{/align_right}', '{bullets}',
                                    '{/bullets}']

    commands = ['word']
    commands_helpers = ['document', 'create', 'new', 'open']

    def __init__(self, text):
        self.text = text

    def translate_for_word(self, text):
        for i in range(0, len(text)):
            if text[i] == 'word':
                if text[i - 1] == 'new' or text[i - 1] == 'create' or (
                        text[i - 2] == 'new' and text[i - 1] == 'empty') or (
                        text[i - 2] == 'create' and text[i - 1] == 'empty') or (
                        text[i - 3] == 'create' and text[i - 2] == 'new' and text[i - 1] == 'empty'):
                    return '{new_word}'
        return ''

    def translate_for_save(self, text):
        for i in range(0, len(text)):
            if text[i] == 'word':
                if text[i - 1] == 'new' or text[i - 1] == 'create' or (
                        text[i - 2] == 'new' and text[i - 1] == 'empty') or (
                        text[i - 2] == 'create' and text[i - 1] == 'empty') or (
                        text[i - 3] == 'create' and text[i - 2] == 'new' and text[i - 1] == 'empty'):
                    return '{new_word}'
        return ''

    def contains_text(self):
        print('function')
        actions = []
        for index in range(0, len(self.available_actions)):
            if self.available_actions[index] in self.text:
                actions.append(self.available_actions_translated[index])
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

    def execute(self, text, obj, word):
        split_text = text.split()
        for word in split_text:
            to_write = self.compare_text(obj, word)
            if word:
                to_write.replace(' ', '')
                obj.write_text(to_write)
            else:
                obj.write_text(to_write + ' ')
