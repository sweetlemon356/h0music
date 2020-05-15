class Musics:
    def __init__(self, name, author, track):
        self.name = name
        self.author = author
        self.track = track

    def play_music(self):
        self.author.play()
