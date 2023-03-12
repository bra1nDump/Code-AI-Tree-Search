
# Solution

def solve(n, t, songs):
    dp = [[[0 for _ in range(3)] for _ in range(t + 1)] for _ in range(n + 1)]
    dp[0][0] = [1, 1, 1]
    for i in range(1, n + 1):
        for j in range(t + 1):
            if j >= songs[i - 1][0]:
                dp[i][j][0] = dp[i - 1][j - songs[i - 1][0]][0] + dp[i - 1][j - songs[i - 1][0]][1] + dp[i - 1][j - songs[i - 1][0]][2]
                dp[i][j][1] = dp[i - 1][j - songs[i - 1][0]][0] + dp[i - 1][j - songs[i - 1][0]][2]
                dp[i][j][2] = dp[i - 1][j - songs[i - 1][0]][0] + dp[i - 1][j - songs[i - 1][0]][1]
            else:
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1] + dp[i - 1][j][2]
                dp[i][j][1] = dp[i - 1][j][0] + dp[i - 1][j][2]
                dp[i][j][2] = dp[i - 1][j][0] + dp[i - 1][j][1]
            dp[i][j][songs[i - 1][1] - 1] -= dp[i - 1][j][songs[i - 1][1] - 1]
            dp[i][j] = [x % (10 ** 9 + 7) for x in dp[i][j]]
    return dp[n][t][0]

n, t = map(int, input().split())
songs = []
for _ in range(n):
    songs.append(list(map(int, input().split())))
print(solve(n, t, songs))