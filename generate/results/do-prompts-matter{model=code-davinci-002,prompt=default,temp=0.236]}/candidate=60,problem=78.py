
import sys

def main():
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])
    songs.sort()

    # dp[i][j][k] = number of ways to make a playlist of length j using songs i, i+1, ..., n-1
    # where k is the genre of the last song in the playlist
    dp = [[[0 for k in range(4)] for j in range(T+1)] for i in range(n)]

    # base case: dp[n-1][j][k] = 1 if j = t_n-1 and k = g_n-1, else 0
    for j in range(T+1):
        for k in range(4):
            if j == songs[n-1][0] and k == songs[n-1][1]:
                dp[n-1][j][k] = 1
            else:
                dp[n-1][j][k] = 0

    # dp[i][j][k] = sum(dp[i+1][j-t_i][g_i]) for all g_i != k
    for i in range(n-2, -1, -1):
        for j in range(T+1):
            for k in range(4):
                if j >= songs[i][0]:
                    for g in range(1, 4):
                        if g != k:
                            dp[i][j][k] += dp[i+1][j-songs[i][0]][g]
                else:
                    dp[i][j][k] = 0

    # sum(dp[0][T][k]) for all k
    ans = 0
    for k in range(4):
        ans += dp[0][T][k]

    print(ans)

if True:
    main()