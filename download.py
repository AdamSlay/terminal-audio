import pafy
import simpleaudio as sa
import moviepy.editor as moviepy
import tempfile
import os

from playsong import PlaySong

class DownloadNew():

    def __init__(self, url):
        print('downloading...')
        self.clip = pafy.new(url)
        self.name = ''.join(self.clip.title.split(' '))
        fname = ''
        for letter in self.name:
            if letter.isalpha():
                fname += letter
            if len(fname) > 29:
                break
        self.filename = f'{fname}.wav'

        try:
            os.remove('temp/tempdir')
        except FileNotFoundError:
            pass

        with tempfile.TemporaryFile(dir='temp') as tempdir:
            self.clip.getbestaudio().download('temp/tempdir', quiet=True)
            audio_clip = moviepy.AudioFileClip('temp/tempdir')
            audio_clip.write_audiofile(f'tracks/{self.filename}')
            os.remove('temp/tempdir')

        print('File has been downloaded')

#DownloadNew('https://www.youtube.com/watch?v=N0OTQbXlM8U')
