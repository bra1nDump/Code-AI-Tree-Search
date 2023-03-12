
import sys

def main():
    """
    The only difference between easy and hard versions is constraints.
    """
    # parse input
    n, T = [int(x) for x in sys.stdin.readline().strip().split()]
    songs = [tuple(int(x) for x in sys.stdin.readline().strip().split()) for _ in range(n)]
    assert(len(songs) == n)
    assert(1 <= T <= 225)
    assert(all(1 <= t <= 15 and 1 <= g <= 3 for t, g in songs))

    # solve
    num_playlists = solve(n, T, songs)

    # output
    print(num_playlists % (10**9 + 7))

def solve(n, T, songs):
    """
    Solves this problem.
    """
    # count the number of times each duration occurs
    # and the number of times each genre occurs
    duration_counts = [0 for _ in range(16)]
    genre_counts = [0 for _ in range(4)]
    for t, g in songs:
        duration_counts[t] += 1
        genre_counts[g] += 1

    # count the number of durations that occur
    num_durations = 0
    for duration_count in duration_counts:
        if duration_count > 0:
            num_durations += 1

    # count the number of genres that occur
    num_genres = 0
    for genre_count in genre_counts:
        if genre_count > 0:
            num_genres += 1

    # if there are no songs, then the number of playlists
    # is zero
    if n == 0:
        return 0

    # if there is only one song, then the number of playlists
    # is one iff its duration is T
    if n == 1:
        if songs[0][0] == T:
            return 1
        else:
            return 0

    # if there are two songs, then the number of playlists
    # is the number of ways to choose the durations of the two
    # songs, which is the product of the number of ways to choose
    # each duration
    if n == 2:
        return duration_counts[T] * duration_counts[T]

    # if there are three songs, then the number of playlists
    # is the number of ways to choose the durations of the three
    # songs, which is the product of the number of ways to choose
    # each duration
    if n == 3:
        return duration_counts[T] * duration_counts[T] * duration_counts[T]

    # if there are at least four songs, then the number of playlists
    # is the sum of the number of playlists for each possible duration
    # of the first song
    num_playlists = 0
    for i in range(1, T//2 + 1):
        # the number of playlists with the first song of duration i
        # is the number of ways to choose the genres of the first three
        # songs, times the number of ways to choose the durations of the
        # remaining songs, times the number of ways to choose the genres
        # of the remaining songs
        num_playlists += (genre_counts[1] * genre_counts[2] * genre_counts[3]) \
                         * (duration_counts[i] * duration_counts[T-i]) \
                         * solve(n - 2, T - i, songs[2:])

    return num_playlists

if True:
    main()