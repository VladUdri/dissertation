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
    start.open_app()
    sleep(1)
    start.create_blank_docx()
    sleep(1)
    # start.save(save_name, 'change name', newname)

    text = 'Seen from a boat, approaching the island through cold, choppy, white-flecked seas, write bold the island of Staffa end bold looks like a dense grey forest of rock off the western coast of Scotland. Columns of basalt push up and then flower out into a puffy, cloud-like summit on top of which the plant life of the island grows, a rolling plain of grass and heather and machair whipped by the sea-wind. write italic The island is made of very ancient rock end italic, but is so strange-looking and so dynamic that you have to tell yourself, repeatedly, that it has been here for a long, long time, such a long time that the best guesses of humankind as to its age can only approximate a range of years that could encompass, with ease, every meaningful incident of human civilisation.'
    sleep(1)
    translated_text = Commands(text=text)
    res = translated_text.contains_text()
    sleep(1)
    translated_text.execute(res, start)
