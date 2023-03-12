
import sys
import math

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    songs = sorted(songs, key=lambda x: x[0])
    dp = [[0 for _ in range(T+1)] for _ in range(n)]
    MOD = 10**9 + 7
    for i in range(n):
        for j in range(T+1):
            if i == 0:
                if j >= songs[i][0]:
                    dp[i][j] = 1
            else:
                if j >= songs[i][0]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
                    if songs[i][1] == songs[i-1][1]:
                        dp[i][j] -= dp[i-2][j-songs[i][0]]
                else:
                    dp[i][j] = dp[i-1][j]
            dp[i][j] %= MOD
    print(dp[n-1][T])

if True:
    main()