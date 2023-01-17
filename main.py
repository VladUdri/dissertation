from word import Word
from time import sleep
from nltk.tokenize import sent_tokenize, word_tokenize
from execution import verify_translation_execute

if __name__ == "__main__":
    memory = []
    start = Word('word')
    i = 0
    title = 'Random writing'
    while True:
        i += 1
        short_term_text = start.get_text(title, title)
        tokenized_text = word_tokenize(short_term_text)
        memory.append(tokenized_text)
        exec = verify_translation_execute(tokenized_text)
        memory.append(exec)
        if i == 5:
            break
