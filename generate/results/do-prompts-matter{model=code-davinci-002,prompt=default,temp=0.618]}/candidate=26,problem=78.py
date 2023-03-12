

def read_input_data():
    n_t = input()
    n, t = int(n_t.split()[0]), int(n_t.split()[1])

    songs = []
    for _ in range(n):
        song_data = input()
        songs.append([int(song_data.split()[0]), int(song_data.split()[1])])
    return n, t, songs


def solve_easy_version(n, t, songs):
    """
    Method solves easy version of problem
    """
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(t + 1):
            dp[i][j] = dp[i - 1][j]
            if j - songs[i - 1][0] >= 0:
                dp[i][j] += dp[i - 1][j - songs[i - 1][0]]
    return dp[n][t]


def solve_hard_version(n, t, songs):
    """
    Method solves hard version of problem
    """
    dp = [[[0] * (t + 1) for _ in range(n + 1)] for _ in range(4)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        for j in range(t + 1):
            dp[songs[i - 1][1]][i][j] = dp[songs[i - 1][1]][i - 1][j]
            if j - songs[i - 1][0] >= 0:
                dp[songs[i - 1][1]][i][j] += dp[songs[i - 1][1]][i - 1][j - songs[i - 1][0]]
            for g in range(1, 4):
                if g != songs[i - 1][1]:
                    dp[g][i][j] = dp[g][i - 1][j]
                    if j - songs[i - 1][0] >= 0:
                        dp[g][i][j] += dp[g][i - 1][j - songs[i - 1][0]]
    return sum(dp[g][n][t] for g in range(1, 4))


def main():
    n, t, songs = read_input_data()
    print(solve_hard_version(n, t, songs))

if True:
    main()