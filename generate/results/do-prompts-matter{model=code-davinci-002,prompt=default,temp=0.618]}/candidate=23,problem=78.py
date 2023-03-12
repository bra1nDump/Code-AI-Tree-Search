
# O(n*T)
def main():
    n, T = (int(x) for x in input().split())
    songs = [None] * n
    for i in range(n):
        t, g = (int(x) for x in input().split())
        songs[i] = (t, g)
    # dp[i][t] - number of playlists of total duration t using songs 1 to i
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for t in range(T + 1):
            dp[i][t] = dp[i - 1][t]
            if t >= songs[i - 1][0]:
                dp[i][t] += dp[i - 1][t - songs[i - 1][0]]
    res = dp[n][T]
    # remove playlists with 2 adjacent songs of the same genre
    for i in range(1, n + 1):
        for t in range(T):
            if songs[i - 1][1] == songs[i - 2][1] and songs[i - 1][0] + t <= T:
                res -= dp[i - 2][t]
    print(res)


main()