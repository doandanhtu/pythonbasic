class Song:
    def __init__(self, name, artist, album, playlist):
        self.name = name
        self.artist = artist
        self.album = album
        self.playlist = playlist
        artist.addSong(self)
        album.addSong(self)
        playlist.addSong(self)

class Album:
    def __init__(self, name):
        self.name = name
        self.song = []

    def addSong(self):


class Artist:
    def __init__(self, name):
        self.name = name
        self.song = []
        self.album = []

    def addSong(self, name: Song):
        return self.song.append(name)

    def addAlbum(self, name: Album):