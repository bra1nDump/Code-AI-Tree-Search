
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        songs.append((t, g))
    songs.sort()
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(T + 1):
            if j >= songs[i - 1][0]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][T])

if True:
    main()