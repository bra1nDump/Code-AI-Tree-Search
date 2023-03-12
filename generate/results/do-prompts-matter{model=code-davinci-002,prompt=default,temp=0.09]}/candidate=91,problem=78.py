
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    dp = [[0 for i in range(T+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(T+1):
            if j >= songs[i][0]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n-1][T])

if True:
    main()