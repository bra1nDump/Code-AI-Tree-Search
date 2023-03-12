
import copy
import math

class Song(object):
    """
    class for a song
    """
    def __init__(self, duration, genre):
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.duration} {self.genre}"

    def __repr__(self):
        return self.__str__()

class Playlist(object):
    """
    class for a playlist of songs
    """
    def __init__(self, songs):
        self.songs = songs
        self.duration = sum([x.duration for x in self.songs])

    def __str__(self):
        return f"{self.duration} {self.songs}"

    def __repr__(self):
        return self.__str__()


def get_playlists(songs, T):
    """
    get playlists of songs that sum to T
    """
    if len(songs) == 0:
        return []
    if len(songs) == 1:
        if songs[0].duration == T:
            return [Playlist([songs[0]])]
        else:
            return []

    # call with one less song
    playlists_one_less = get_playlists(songs[1:], T)

    # call with one more
    playlists_one_more = get_playlists(songs[1:], T - songs[0].duration)
    for playlist in playlists_one_more:
        playlist.songs.append(songs[0])
        playlist.duration += songs[0].duration

    return playlists_one_less + playlists_one_more


def remove_duplicates(playlists):
    """
    remove duplicate playlists from a list of playlists
    """
    playlists_copy = copy.deepcopy(playlists)
    for playlist_idx in range(len(playlists)):
        for playlist_copy_idx in range(playlist_idx + 1, len(playlists_copy)):
            if playlists[playlist_idx].songs == playlists_copy[playlist_copy_idx].songs:
                playlists_copy.pop(playlist_copy_idx)
                break
    return playlists_copy


def remove_repeats(playlists):
    """
    remove playlists with adjacent songs of the same genre
    """
    playlists_copy = copy.deepcopy(playlists)
    for playlist_idx in range(len(playlists)):
        for song_idx in range(len(playlists[playlist_idx].songs) - 1):
            if playlists[playlist_idx].songs[song_idx].genre == playlists[playlist_idx].songs[song_idx + 1].genre:
                playlists_copy.pop(playlist_idx)
                break
    return playlists_copy


def count_playlists(playlists):
    """
    count the number of unique playlists
    """
    modulo = 1000000007
    unique_playlists = remove_duplicates(playlists)
    unique_playlists = remove_repeats(unique_playlists)
    unique_playlists = remove_duplicates(unique_playlists)
    return len(unique_playlists) % modulo


if True:
    n, T = [int(x) for x in input().strip().split(" ")]
    songs = []
    for _ in range(n):
        duration, genre = [int(x) for x in input().strip().split(" ")]
        songs.append(Song(duration, genre))
    playlists = get_playlists(songs, T)
    # print(playlists)
    print(count_playlists(playlists))