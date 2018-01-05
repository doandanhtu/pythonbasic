class Song:

    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number

        artist.add_song(self)


class Album:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

        self.tracks = []

        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)

        song = Song(title, artist, self, track_number)

        self.tracks.append(song)


class Artist:
    def __init__(self, name):
        self.name = name

        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

lkp = Artist('Linkin Park')
ht = Album('Hybrid Theory', lkp, 2000)
ite = Song('In the End', lkp, ht, 8)


pl = Playlist('DanII')

