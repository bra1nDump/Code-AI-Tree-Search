
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])
    dp = [[0] * (T + 1) for _ in range(n)]
    dp[0][songs[0][0]] = 1
    for i in range(1, n):
        for j in range(T + 1):
            if dp[i - 1][j] > 0:
                if j + songs[i][0] <= T:
                    dp[i][j + songs[i][0]] += dp[i - 1][j]
                if j + songs[i][0] <= T and songs[i][1] != songs[i - 1][1]:
                    dp[i][j + songs[i][0]] += dp[i - 1][j]
    print(dp[n - 1][T])

if True:
    main()