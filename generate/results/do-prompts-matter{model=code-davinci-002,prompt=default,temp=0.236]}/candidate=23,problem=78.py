
import sys

def main():
    # read input
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])
    # print(n, T, songs)

    # create a list of songs for each genre
    songs_by_genre = [[] for i in range(4)]
    for i in range(n):
        songs_by_genre[songs[i][1]].append(songs[i])

    # create a list of all possible playlists
    playlists = []
    for i in range(1, 4):
        playlists += create_playlists(songs_by_genre[i], T)
    # print(playlists)

    # count the number of unique playlists
    unique_playlists = []
    for playlist in playlists:
        if playlist not in unique_playlists:
            unique_playlists.append(playlist)
    # print(unique_playlists)

    print(len(unique_playlists))


def create_playlists(songs, T):
    playlists = []
    for i in range(len(songs)):
        if songs[i][0] == T:
            playlists.append([songs[i]])
        elif songs[i][0] < T:
            for playlist in create_playlists(songs[i+1:], T-songs[i][0]):
                playlists.append([songs[i]] + playlist)
    return playlists


if True:
    main()