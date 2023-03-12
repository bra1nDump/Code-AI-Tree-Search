
import sys

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split(' ')))

def get_playlist_count(n, t, song_lengths, song_genres):
    # Let's pad the song lengths with a 0 at the start to make indexing easier.
    # This 0 is for the case where the first song doesn't play.
    song_lengths = [0] + song_lengths

    # Let's also pad the song genres with a 0 at the start to make indexing easier.
    # This 0 is for the case where the first song doesn't play.
    song_genres = [0] + song_genres

    # Create a matrix of size (n+1) x (t+1) to store the number of playlists
    # that can be created with the first i songs and d duration.
    # The values of this matrix will be calculated bottom-up.
    playlist_count = [[0] * (t+1) for _ in range(n+1)]

    # The number of playlists that can be created with the first song and d
    # duration is 1 if song_lengths[1] == d, and 0 otherwise.
    for d in range(1, t+1):
        playlist_count[1][d] = 1 if song_lengths[1] == d else 0

    # Fill the rest of the matrix.
    # The number of playlists that can be created with the first i songs and d
    # duration is the sum of two terms.
    #
    # First term: the number of playlists that can be created with the first i
    # songs and d-song_lengths[i] duration. This term is calculated by
    # playlist_count[i][d-song_lengths[i]].
    #
    # Second term: the number of playlists that can be created with the first i
    # songs and d duration and the i-th song plays last. This term is calculated
    # with the help of another matrix.
    #
    # This new matrix has the same dimensions as playlist_count, and it stores
    # the number of playlists that can be created with the first i songs and d
    # duration, and the i-th song plays last.
    for i in range(2, n+1):
        for d in range(1, t+1):
            playlist_count[i][d] = playlist_count[i][d-song_lengths[i]]

            if d >= song_lengths[i]:
                if song_genres[i-1] != song_genres[i]:
                    playlist_count[i][d] += playlist_count[i-1][d-song_lengths[i]]

    return playlist_count[n][t]

def main():
    n, t = read_ints()
    song_lengths = read_ints()
    song_genres = read_ints()

    print(get_playlist_count(n, t, song_lengths, song_genres))

if True:
    main()