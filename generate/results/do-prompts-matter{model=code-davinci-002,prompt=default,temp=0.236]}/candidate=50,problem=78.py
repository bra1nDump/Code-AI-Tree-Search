

# Solution

import sys

def solve(n, T, songs):
    """
    >>> solve(3, 3, [(1, 1), (1, 2), (1, 3)])
    6
    >>> solve(3, 3, [(1, 1), (1, 1), (1, 3)])
    2
    >>> solve(4, 10, [(5, 3), (2, 1), (3, 2), (5, 1)])
    10
    """
    # dp[i][j] = number of playlists of length i ending with genre j
    dp = [[0] * 4 for _ in range(T+1)]
    dp[0][0] = 1
    for i in range(1, T+1):
        for j in range(1, 4):
            for song in songs:
                if song[0] == i and song[1] == j:
                    for k in range(1, 4):
                        dp[i][j] += dp[i-song[0]][k]
    return sum(dp[T]) % (10**9 + 7)

if True:
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))