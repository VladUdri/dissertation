import pyautogui as pg
from time import sleep
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import re


class Commands():
    available_actions = ['write bold', 'end bold', 'write italic', 'end italic', 'write underlined', 'end underlined',
                         'align justify', 'end justify', 'align center', 'end center',
                         'align left', 'end left', 'align right', 'end right', 'add bullets', 'end bullets']
    available_actions_translated = ['{bold}', '{/bold}', '{italic}', '{/italic}', '{underlined}', '{/underlined}',
                                    '{align_justify}', '{/align_justify}',
                                    '{align_center}', '{/align_center}',
                                    '{align_left}', '{/align_left}', '{align_right}', '{/align_right}', '{bullets}',
                                    '{/bullets}']

    comm = {'word': True, 'save': True, 'write': True, 'writing': True, 'volume': True, 'brightness': True,
            'outlook': True, 'email': True, 'edit': True}

    action_translation_one_word = {'bold': {'exists': False, 'activate': '{bold}', 'inactivate': '{/bold}'},
                                   'italic': {'exists': False, 'activate': '{italic}', 'inactivate': '{/italic}'},
                                   'underlined': {'exists': False, 'activate': '{underlined}',
                                                  'inactivate': '{/underlined}'}}

    align = False
    action_translation_two_words = {'left': '{align_left}',
                                    'right': '{align_right}',
                                    'center': '{align_center}',
                                    'justify': '{align_justify}',
                                    }

    def __init__(self, text):
        self.text = text

    def checker(self):
        for word in range(0, len(self.text)):
            lower_case_text = self.text[word].lower()
            if lower_case_text in self.comm.keys():
                if lower_case_text == 'word':
                    return self.translate_for_word(self.text, word)
                elif lower_case_text == 'save':
                    return self.translate_for_save(self.text, word)
                elif lower_case_text == 'write' or lower_case_text == 'writing':
                    return self.translate_for_write(self.text, word)
                elif lower_case_text == 'volume':
                    return self.translate_for_volume(self.text, word)
                elif lower_case_text == 'brightness':
                    return self.translate_for_brightness(self.text, word)
                elif lower_case_text == 'outlook':
                    return self.translate_for_outlook(self.text, word)
                elif lower_case_text == 'email':
                    return self.translate_for_email(self.text, word)
                elif lower_case_text == 'edit':
                    return self.translate_for_edit(self.text, word)

    def translate_for_word(self, text, i):
        if text[i - 1] == 'new' or text[i - 1] == 'create' or (
                text[i - 2] == 'new' and text[i - 1] == 'empty') or (
                text[i - 2] == 'create' and text[i - 1] == 'empty') or (
                text[i - 3] == 'create' and text[i - 2] == 'new' and text[i - 1] == 'empty'):
            return '{new_word}'
        elif text[i - 1] == 'open' or (text[i - 2] == 'go' and text[i - 1] == 'to'):
            return '{taskbar_word}'  # meaning go to Word window
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

    def translate_for_volume(self, text, i):
        if text[i - 1] == 'increase' or (
                text[i - 2] == 'increase' and text[i - 1] == 'the') or text[i + 1] == 'up':
            return '{volume_up}'
        if text[i - 1] == 'decrease' or (
                text[i - 2] == 'decrease' and text[i - 1] == 'the') or text[i + 1] == 'down':
            return '{volume_down}'
        return ''

    # todo fix "decrease"
    def translate_for_brightness(self, text, i):
        if text[i - 1] == 'increase' or (
                text[i - 2] == 'increase' and text[i - 1] == 'the') or text[i + 1] == 'up':
            return '{brightness_up}'
        if text[i - 1] == 'decrease' or (
                text[i - 2] == 'decrease' and text[i - 1] == 'the') or text[i + 1] == 'down':
            return '{brightness_down}'
        return ''

    def translate_for_outlook(self, text, i):
        if text[i - 1] == 'open' or (text[i - 2] == 'go' and text[i - 1] == 'to'):
            if pg.locateCenterOnScreen('img\\taskbar_outlook.png',
                                       confidence=0.8) is not None or pg.locateCenterOnScreen(
                'img\\taskbar_outlook_empty.png'):
                return '{taskbar_outlook}'
            else:
                return '{new_outlook}'
        return ''

    def translate_for_email(self, text, i):
        if text[i - 1] == 'send' or text[i - 2] == 'send':
            return '{new_email}'
        return ''

    def translate_for_edit(self, text, i):
        if text[i + 1] == 'text':
            return '{edit_word}'
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

    # this will work for words
    # TO BE KEPT
    def convert_text(self, text):
        if text in self.action_translation_one_word.keys():
            if self.action_translation_one_word[text]['exists'] == False:
                self.action_translation_one_word[text]['exists'] = True
                return self.action_translation_one_word[text]['activate']
            else:
                self.action_translation_one_word[text]['exists'] = False
                return self.action_translation_one_word[text]['inactivate']
        elif text == 'align':
            self.align = True
        elif text in self.action_translation_two_words.keys():
            if self.align:
                self.align = False
                return self.action_translation_two_words[text]
        else:
            self.align = False
        return text

    def write_text_new(self, text):
        words = word_tokenize(text)
        new_text = ''
        for word in words:
            converted_word = self.convert_text(word)
            if new_text != '' and converted_word not in string.punctuation:
                new_text += ' '
            new_text += converted_word
        return new_text

    def execute(self, obj, is_word):
        self.contains_text()
        to_write = ''
        split_text = self.text.split()
        for word in split_text:
            to_write = self.compare_text(obj, word)
            if is_word:
                to_write.replace(' ', '')
                obj.write_text(to_write)
            else:
                obj.write_text(to_write + ' ')
        return to_write
