

class Song:
    def __init__(self, duration, genre):
        self.duration = duration
        self.genre = genre

    def __repr__(self):
        return "{} {}".format(self.duration, self.genre)


def get_sequences(songs, time):
    num_sequences = 0
    for song in songs:
        if time - song.duration > 0:
            new_songs = list(filter(lambda s: s.duration <= time and s.genre != song.genre, songs))
            num_sequences += get_sequences(new_songs, time - song.duration)
        if time - song.duration == 0:
            num_sequences += 1
    return num_sequences


def main():
    num_songs, time = [int(x) for x in input().strip().split()]
    songs = []
    for i in range(num_songs):
        duration, genre = [int(x) for x in input().strip().split()]
        songs.append(Song(duration, genre))
    print(get_sequences(songs, time))


if True:
    main()