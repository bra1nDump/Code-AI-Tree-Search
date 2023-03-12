

def main():
    n, t = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))
    # print(songs)
    # print(t)

    # dp[i][j] = number of ways to create a playlist of length j using songs 0 to i
    # dp[i][j] = sum(dp[i-1][j-k]) for k in range(t_i, j+1) if g_i != g_(i-1)
    # dp[i][j] = sum(dp[i-1][j-k]) for k in range(t_i, j+1) if g_i == g_(i-1) and j-k != t_(i-1)
    # dp[i][j] = 0 if j < t_i

    dp = [[0 for _ in range(t+1)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        t_i, g_i = songs[i]
        for j in range(t+1):
            if j < t_i:
                dp[i][j] = 0
            else:
                t_prev, g_prev = songs[i-1]
                if g_i != g_prev:
                    dp[i][j] = sum(dp[i-1][j-k] for k in range(t_i, j+1))
                else:
                    dp[i][j] = sum(dp[i-1][j-k] for k in range(t_i, j+1) if k != t_prev)
    # print(dp)
    print(dp[n-1][t])


if True:
    main()