
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    dp = [[[0 for _ in range(T+1)] for _ in range(3)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(3):
            for k in range(T+1):
                if j == songs[i-1][1]:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][songs[i-1][1]][k-songs[i-1][0]]
    print(dp[n][0][T] + dp[n][1][T] + dp[n][2][T])

if True:
    main()