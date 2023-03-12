
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    # print(songs)
    dp = [[0 for i in range(T+1)] for j in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(T+1):
            if j >= songs[i][0]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    print(dp[n-1][T])

if True:
    main()