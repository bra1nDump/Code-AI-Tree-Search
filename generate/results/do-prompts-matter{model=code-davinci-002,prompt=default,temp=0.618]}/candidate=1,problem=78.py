
import collections
import copy

n, T = map(int, input().split())
songs = []
for i in range(n):
    t, g = map(int, input().split())
    songs.append((t, g))


def play_song(song, prev_song):
    if prev_song is None:
        return True
    if song[1] == prev_song[1]:
        return False
    return True


def play_playlist(playlist, prev_playlist):
    if prev_playlist is None:
        return True
    if len(playlist) != len(prev_playlist):
        return False
    for i in range(len(playlist)):
        if playlist[i][0] != prev_playlist[i][0]:
            return False
        if playlist[i][1] == prev_playlist[i][1]:
            return False
    return True


def play_playlists(playlists, prev_playlists):
    if prev_playlists is None:
        return True
    if len(playlists) != len(prev_playlists):
        return False
    for i in range(len(playlists)):
        if play_playlist(playlists[i], prev_playlists[i]) is False:
            return False
    return True


def dfs(songs, playlists, time_left, prev_playlists):
    if time_left == 0:
        if play_playlists(playlists, prev_playlists) is True:
            return 1
        else:
            return 0
    if len(songs) == 0:
        return 0

    num_playlists = 0
    for i in range(len(songs)):
        new_playlists = copy.deepcopy(playlists)
        new_playlists.append(songs[i])
        num_playlists += dfs(songs[:i] + songs[i + 1:], new_playlists, time_left - songs[i][0], playlists)

    return num_playlists


def main():
    num_playlists = 0
    for i in range(len(songs)):
        num_playlists += dfs(songs[:i] + songs[i + 1:], [songs[i]], T - songs[i][0], None)
    print(num_playlists)


if True:
    main()