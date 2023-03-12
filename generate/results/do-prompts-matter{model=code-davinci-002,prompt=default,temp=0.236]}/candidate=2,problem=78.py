
import sys

def main():
    # Read the input
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))

    # Create a list of songs for each genre
    songs_by_genre = [[] for i in range(3)]
    for i in range(n):
        songs_by_genre[songs[i][1] - 1].append(songs[i][0])

    # Create a list of all possible playlists
    playlists = []
    for i in range(3):
        playlists.append(create_playlists(songs_by_genre[i], T))

    # Count the number of different playlists
    count = 0
    for i in range(len(playlists[0])):
        for j in range(len(playlists[1])):
            for k in range(len(playlists[2])):
                if len(playlists[0][i]) + len(playlists[1][j]) + len(playlists[2][k]) == T:
                    count += 1

    # Print the result
    print(count)

def create_playlists(songs, T):
    """
    Creates a list of all possible playlists of songs with a total duration of T.
    """
    playlists = []
    for i in range(len(songs)):
        if songs[i] == T:
            playlists.append([i])
        elif songs[i] < T:
            for playlist in create_playlists(songs[i + 1:], T - songs[i]):
                playlists.append([i] + playlist)
    return playlists

if True:
    main()