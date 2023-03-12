
def main():
    """
    0:15
    0:30
    1:00
    1:15
    1:30
    2:00
    2:15
    2:30
    3:00
    3:15
    3:30
    4:00
    4:15
    4:30
    5:00
    """
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))
    songs.sort()

    dp = [[[0 for _ in range(4)] for _ in range(T + 1)] for _ in range(n)]

    for i in range(4):
        dp[0][songs[0][0]][i] = 1

    for i in range(1, n):
        for t in range(T + 1):
            for g in range(4):
                if t >= songs[i][0]:
                    dp[i][t][g] = sum(dp[i - 1][t - songs[i][0]][g_i] for g_i in range(4))
                else:
                    dp[i][t][g] = 0
                if g == songs[i][1]:
                    dp[i][t][g] -= sum(dp[i - 1][t - songs[i][0]][g_i] for g_i in range(4) if g_i == g)
    print(sum(dp[n - 1][T][g] for g in range(4)))


if True:
    main()