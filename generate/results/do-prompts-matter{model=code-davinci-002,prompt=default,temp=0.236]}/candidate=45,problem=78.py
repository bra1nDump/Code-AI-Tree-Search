
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        songs.append((t, g))
    songs.sort()
    dp = [[[0 for _ in range(T + 1)] for _ in range(4)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(T + 1):
                if dp[i][j][k] != 0:
                    dp[i + 1][j][k] += dp[i][j][k]
                    if k + songs[i][0] <= T:
                        dp[i + 1][songs[i][1]][k + songs[i][0]] += dp[i][j][k]
    print(dp[n][0][T])

if True:
    main()