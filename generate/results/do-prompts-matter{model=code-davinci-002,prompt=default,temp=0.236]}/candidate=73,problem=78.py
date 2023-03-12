
import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(songs, t))

def solve(songs, t):
    dp = [[[0 for _ in range(t + 1)] for _ in range(4)] for _ in range(len(songs) + 1)]
    dp[0][0][0] = 1
    for i in range(1, len(songs) + 1):
        for j in range(4):
            for k in range(t + 1):
                if j == songs[i - 1][1]:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][songs[i - 1][1]][k - songs[i - 1][0]]
    return dp[len(songs)][0][t]

if True:
    main()