
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        songs.append((t, g))
    songs.sort()
    print(songs)
    dp = [[0 for j in range(T+1)] for i in range(n)]
    for i in range(n):
        t, g = songs[i]
        dp[i][0] = 1
        for j in range(T+1):
            if j >= t:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-t]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    print(dp[n-1][T])

if True:
    main()