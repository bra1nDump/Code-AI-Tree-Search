
import sys

def main():
    # read input
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])
    #print(songs)
    #print(n, T)

    # create a list of all possible playlists
    playlists = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    playlists.append([i, j, k])
    #print(playlists)

    # create a list of all possible playlists with the correct total duration
    valid_playlists = []
    for playlist in playlists:
        if sum([songs[playlist[i]][0] for i in range(3)]) == T:
            valid_playlists.append(playlist)
    #print(valid_playlists)

    # create a list of all possible playlists with the correct total duration and no repeated songs
    valid_playlists_no_repeats = []
    for playlist in valid_playlists:
        if len(playlist) == len(set(playlist)):
            valid_playlists_no_repeats.append(playlist)
    #print(valid_playlists_no_repeats)

    # create a list of all possible playlists with the correct total duration, no repeated songs, and no two consecutive songs of the same genre
    valid_playlists_no_repeats_no_consecutive_genres = []
    for playlist in valid_playlists_no_repeats:
        if songs[playlist[0]][1] != songs[playlist[1]][1] and songs[playlist[1]][1] != songs[playlist[2]][1]:
            valid_playlists_no_repeats_no_consecutive_genres.append(playlist)
    #print(valid_playlists_no_repeats_no_consecutive_genres)

    # output the number of valid playlists
    print(len(valid_playlists_no_repeats_no_consecutive_genres))

if True:
    main()