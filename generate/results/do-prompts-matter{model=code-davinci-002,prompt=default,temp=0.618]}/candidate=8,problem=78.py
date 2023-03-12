
import sys
sys.path.append('../')

import math


def solve(t, n, songs):
    """
    Args:
        t: total time
        n: number of songs
        songs: list of songs, each song is represented by a tuple of (time, genre)
    Returns:
        int: number of different combinations
    """
    # dp[i][j][k]: number of different combinations of songs up to i
    # ending with j and total time is k, j is a song index
    dp = [[[0 for _ in range(t + 1)] for _ in range(n)] for _ in range(n)]

    for j in range(n):
        # initialize the first song
        dp[0][j][songs[j][0]] = 1

    for i in range(1, n):
        for j in range(n):
            for k in range(t + 1):
                dp[i][j][k] = 0
                if k < songs[j][0]:
                    continue
                for l in range(n):
                    if l == j or songs[l][1] == songs[j][1]:
                        continue
                    dp[i][j][k] += dp[i - 1][l][k - songs[j][0]]

    return sum(sum(dp[n - 1][j]) for j in range(n))


def test():
    assert solve(3, 3, [(1, 1), (1, 2), (1, 3)]) == 6
    assert solve(3, 3, [(1, 1), (1, 1), (1, 3)]) == 2
    assert solve(10, 4, [(5, 3), (2, 1), (3, 2), (5, 1)]) == 10

    # from random import randint
    # for _ in range(10):
    #     t = randint(1, 225)
    #     n = randint(1, 15)
    #     songs = []
    #     for _ in range(n):
    #         t_i = randint(1, 15)
    #         g_i = randint(1, 3)
    #         songs.append((t_i, g_i))
    #     print(t, n, songs)
    #     print(solve(t, n, songs))


if True:
    # test()

    n, t = list(map(int, input().split()))
    songs = []
    for _ in range(n):
        t_i, g_i = list(map(int, input().split()))
        songs.append((t_i, g_i))
    print(solve(t, n, songs))