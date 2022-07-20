import simpleaudio as sa

class PlaySong():

    def __init__(self, filename):
        sa.stop_all()
        self.track = sa.WaveObject.from_wave_file(f'tracks/{filename}')
        self.track.play()

    def stop(self):
        sa.stop_all()