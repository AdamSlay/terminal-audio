from turtle import done
import urwid
from download import DownloadNew

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.WidgetPlaceholder):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        DownloadNew(q.edit_text)

q = urwid.Edit(u'Enter URL: ')   
'''
edit = urwid.Edit(u'What is your name?\n')
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()
'''


# I am lost. I dont understand how to take input
# and save it to a variable.