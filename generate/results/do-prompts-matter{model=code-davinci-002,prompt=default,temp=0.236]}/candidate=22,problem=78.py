
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    print(songs)
    # dp[i][j] = number of ways to get to time j using songs 0 to i
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t_i]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t_i] - dp[i-1][j-t_i-1]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t_i] - dp[i-1][j-t_i-1]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t_i] - dp[i-1][j-t_i-1]
    dp = [[0 for j in range(T+1)] for i in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= songs[i][0]:
                dp[i][j] += dp[i-1][j-songs[i][0]]
                if j >= songs[i][0]+1:
                    dp[i][j] -= dp[i-1][j-songs[i][0]-1]
    print(dp)
    print(dp[n-1][T])

if True:
    main()