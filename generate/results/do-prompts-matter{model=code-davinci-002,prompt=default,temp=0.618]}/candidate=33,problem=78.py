
import sys

def read_data():
    """
    Reads the data from the file.
    """
    n, t = map(int, input().strip().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, input().strip().split())))
    return n, t, songs


def get_playlists(n, t, songs):
    """
    Calculates the number of different sequences of songs.
    """
    # The dynamic programming array.
    dp = [[[0, 0, 0] for j in range(t + 1)] for i in range(n + 1)]

    # Base cases.
    for i in range(1, n + 1):
        for j in range(songs[i - 1][0], t + 1):
            if i == 1:
                dp[i][j][songs[i - 1][1] - 1] = 1
            else:
                # Calculate the number of playlists which end with the current song.
                for k in range(songs[i - 1][0], j + 1):
                    for l in range(3):
                        if l != songs[i - 1][1] - 1:
                            dp[i][j][songs[i - 1][1] - 1] += dp[i - 1][k - songs[i - 1][0]][l]
    # The total number of playlists.
    return sum(dp[n][t]) % (10**9 + 7)


def main():
    """
    The main function.
    """
    n, t, songs = read_data()
    print(get_playlists(n, t, songs))


if True:
    sys.exit(main())