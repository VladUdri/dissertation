from word import Word
from time import sleep
from commands import Commands

if __name__ == "__main__":
    # save_name = 'test 1234'
    # newname = 'test 1234'
    # bold = '{bold}'
    # end_bold = '{/bold}'
    # words = []
    # write_text = True
    # bold_text = 'Ana'
    #
    start = Word('word')
    # start.open_app()
    # sleep(1)
    # start.create_blank_docx()
    sleep(1)
    # start.save(save_name, 'change name', newname)
    # sleep(1)
    # text =  'Seen from a boat, approaching the island through cold, choppy, white-flecked seas, the island of Staffa looks like a dense grey forest of rock off the western coast of Scotland. Columns of basalt push up and then flower out into a puffy, cloud-like summit on top of which the plant life of the island grows, a rolling plain of grass and heather and machair whipped by the sea-wind.'
    # start.write_text(text)
    comm = 'write bold write italic and'
    translated_text = Commands(comm)
    start.find_edit_words('and', comm, start)
    # res = translated_text.contains_text()
    # sleep(1)
    # translated_text.execute(res, start)
