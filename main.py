from word import Word
from time import sleep

if __name__ == "__main__":
    save_name = 'test 1234'
    newname = 'test 1234'
    bold = '{bold}'
    end_bold = '{/bold}'
    words = []
    write_text = True
    bold_text = 'Ana'

    start = Word('word')
    start.open_app()
    sleep(1)
    start.create_blank_docx()
    sleep(1)
    # start.save(save_name, 'change name', newname)

    while True:
        if (write_text):
            text = start.get_text()

        if 'stop' == text:
            write_text = False
        elif bold in text:
            start.change_to_bold()
            text = text.replace(bold, '')
            words.append(text)
            start.write_text(text)
            start.change_to_bold()
        else:
            words.append(text)
            start.write_text(text)
        print(len(words))
        if (len(words) >= 5):
            break
        elif (len(words) == 3):
            print(words)


