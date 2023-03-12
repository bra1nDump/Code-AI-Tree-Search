
#python3
import sys


def read_data():
    n, t = map(int, input().split())
    songs = [tuple(map(int, input().split())) for _ in range(n)]
    return n, t, songs


def get_correct_playlists(n, t, songs):
    if t > sum(song[0] for song in songs):
        return 0
    elif t == sum(song[0] for song in songs):
        return 1

    if not songs:
        return 0
    total = 0
    for i in range(len(songs)):
        if songs[i][0] == t:
            total += 1
        else:
            total += get_correct_playlists(n, t - songs[i][0], songs[i + 1:])
    return total


def main():
    n, t, songs = read_data()
    print(get_correct_playlists(n, t, songs) % (10 ** 9 + 7))


if True:
    main()