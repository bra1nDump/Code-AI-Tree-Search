
import sys
from collections import defaultdict


def inp():
    return sys.stdin.readline().strip()


def solve(n, t, songs):
    # dp[i][j][k]: # of ways to make playlist of length i, ending with song of genre k
    dp = [[[0 for _ in range(4)] for _ in range(t+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0][0] = 1
    for i in range(1, n+1):
        for j in range(1, t+1):
            for k in range(4):
                if j - songs[i][0] >= 0:
                    dp[i][j][k] = (dp[i-1][j][k] + dp[i-1][j-songs[i][0]][songs[i][1]]) % 1000000007
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    return dp[n][t][0]
    

def main():
    n, t = [int(x) for x in inp().split()]
    songs = [[0, 0]]
    for i in range(n):
        songs.append([int(x) for x in inp().split()])
    print(solve(n, t, songs))


if True:
    main()