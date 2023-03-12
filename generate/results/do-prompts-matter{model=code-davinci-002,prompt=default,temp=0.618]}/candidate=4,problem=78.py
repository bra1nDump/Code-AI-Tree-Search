

def solve(n, t, songs):
    dp = [[[0 for _ in range(t + 1)] for _ in range(3)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            for k in range(3):
                if j - songs[i][0] < 0:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    if k == songs[i][1] - 1:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        if j - songs[i][0] == 0:
                            dp[i][j][k] = dp[i - 1][j][k] + 1
                        else:
                            dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - songs[i][0]][songs[i][1] - 1]
    return sum(dp[n][t]) % (10 ** 9 + 7)


def main():
    n, t = map(int, input().split())
    songs = [[0, 0]]
    for i in range(n):
        t_i, g_i = map(int, input().split())
        songs.append([t_i, g_i])
    print(solve(n, t, songs))


if True:
    main()