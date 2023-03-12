
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    songs.sort(key=lambda x: x[0])
    dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            if j >= songs[i - 1][0]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[-1][-1])

if True:
    main()