import os
import urwid

from download import DownloadNew
from playsong import PlaySong
from question import QuestionBox

tracks = sorted(os.listdir(path='tracks'))
playlists = sorted(os.listdir(path='playlists'))
url_req = urwid.Edit(u'Please enter the URL: ') # placeholder line 53
a_track = 'Are you downloading a track?'

down = input('First off, are you wanting to download a new file? y/n\n')
if down == 'y':
    url = input('Enter the URL here: ')
    DownloadNew(url)
else:
    pass

def menu_button(caption, callback, *args):
    button = urwid.Button(caption)
    if args:
        urwid.connect_signal(button, 'click', callback, args[0])
    else:
        urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, u'...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def song_chosen(button):
    response = urwid.Text([u'Now Playing: \n\n', button.label, u'\n\n'])
    track = PlaySong(button.label)
    stop_play = menu_button(u'Stop Playback', stop_playback, track)
    done = menu_button(u'Quit', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, stop_play, done])))

def playlist_chosen(button):
    pass

def exit_program(button):
    raise urwid.ExitMainLoop()

def as_url(button):
    q, size = urwid.Edit(u'Enter URL: ') , (20,)
    done = menu_button(u'Done', QuestionBox, q.edit_text)
    top.open_box(urwid.Filler(urwid.Pile([q, done])))
    #DownloadNew(url)

def stop_playback(button, track):
    track.stop()
    pass

menu_top = menu(u'Main Menu', [

            sub_menu(u'Listen', [
                sub_menu(u'Tracks', [menu_button(track, song_chosen) for track in tracks]),
                sub_menu(u'Playlists', [menu_button(playlist, playlist_chosen) for playlist in playlists])]),

            #sub_menu(u'Download', [menu_button(a_track, as_url)]),

            sub_menu(u'Quit', [('Are you sure?', menu_button(u'quit', exit_program))])
        ]
    )


class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'\N{MEDIUM SHADE}'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level * 3,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

top = CascadingBoxes(menu_top)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
