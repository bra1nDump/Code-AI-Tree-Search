
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int():
    return int(sys.stdin.readline())

def main():
    n, T = read_ints()
    songs = []
    for _ in range(n):
        songs.append(read_ints())
    # print(songs)

    # dp[i][j] is the number of ways to play songs of total length j using the first i songs
    dp = [[0 for j in range(T+1)] for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= songs[i-1][0]:
                dp[i][j] += dp[i-1][j-songs[i-1][0]]

    # print(dp)

    # dp2[i][j] is the number of ways to play songs of total length j using the first i songs
    # such that the last two songs are not of the same genre
    dp2 = [[0 for j in range(T+1)] for i in range(n+1)]
    dp2[0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            dp2[i][j] = dp2[i-1][j]
            if j >= songs[i-1][0]:
                dp2[i][j] += dp2[i-1][j-songs[i-1][0]]
                if i >= 2 and songs[i-1][1] != songs[i-2][1]:
                    dp2[i][j] += dp2[i-2][j-songs[i-1][0]]

    # print(dp2)

    ans = dp2[n][T]
    for i in range(n):
        ans -= dp2[i][T]
    print(ans)

if True:
    main()