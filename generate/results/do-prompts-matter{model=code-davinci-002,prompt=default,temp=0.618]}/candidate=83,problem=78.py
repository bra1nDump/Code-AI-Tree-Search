
import sys


def solve(n, t, songs):
    max_duration = max(songs[:, 0])
    if t < max_duration:
        return 0
    n_genres = max(songs[:, 1])
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= songs[i - 1][0]:
                dp[i][j] += dp[i - 1][j - songs[i - 1][0]]
                if songs[i - 1][1] == 1:
                    dp[i][j] += 1
                elif songs[i - 1][1] == 2 and j - songs[i - 1][0] > 0:
                    dp[i][j] += dp[i - 1][j - songs[i - 1][0] - 1]
                elif songs[i - 1][1] == 3 and j - songs[i - 1][0] > 1:
                    dp[i][j] += dp[i - 1][j - songs[i - 1][0] - 2]
    return dp[n][t]


def main():
    stdin = sys.stdin
    n, t = [int(x) for x in stdin.readline().split()]
    songs = [[int(x) for x in stdin.readline().split()] for _ in range(n)]
    songs = np.array(songs, dtype=np.int32)
    print(solve(n, t, songs))


if True:
    main()