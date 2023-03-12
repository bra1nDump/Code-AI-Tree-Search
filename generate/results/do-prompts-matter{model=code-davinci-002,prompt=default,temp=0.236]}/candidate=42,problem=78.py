
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])

    # dp[i][j] = number of ways to make a playlist of length j using songs 0 through i
    dp = [[0 for j in range(T+1)] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, T+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= songs[i][0]:
                dp[i][j] += dp[i][j-songs[i][0]]

    # dp2[i][j] = number of ways to make a playlist of length j using songs 0 through i such that the last song is of genre j
    dp2 = [[0 for j in range(T+1)] for i in range(n)]
    for i in range(n):
        dp2[i][0] = 1

    for i in range(n):
        for j in range(1, T+1):
            if i > 0:
                dp2[i][j] = dp2[i-1][j]
            if j >= songs[i][0] and songs[i][1] == j:
                dp2[i][j] += dp2[i][j-songs[i][0]]

    # dp3[i][j] = number of ways to make a playlist of length j using songs 0 through i such that the last two songs are of genre j
    dp3 = [[0 for j in range(T+1)] for i in range(n)]
    for i in range(n):
        dp3[i][0] = 1

    for i in range(n):
        for j in range(1, T+1):
            if i > 0:
                dp3[i][j] = dp3[i-1][j]
            if j >= songs[i][0] and songs[i][1] == j:
                dp3[i][j] += dp3[i][j-songs[i][0]]

    ans = dp[n-1][T]
    for i in range(1, 4):
        ans -= dp2[n-1][i]
    for i in range(1, 4):
        ans += dp3[n-1][i]

    print(ans)

if True:
    main()