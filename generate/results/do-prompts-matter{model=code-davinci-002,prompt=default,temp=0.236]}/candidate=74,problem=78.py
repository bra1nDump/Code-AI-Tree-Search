
# Solution 1
def solve(n, t, songs):
    dp = [[[0] * 4 for _ in range(t + 1)] for _ in range(n + 1)]
    dp[0][0] = [1] * 4
    for i in range(1, n + 1):
        for j in range(t + 1):
            for k in range(1, 4):
                if j - songs[i][0] >= 0:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - songs[i][0]][k]
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
                if songs[i][1] == k:
                    dp[i][j][k] -= dp[i - 1][j - songs[i][0]][k]
    return dp[n][t][1] + dp[n][t][2] + dp[n][t][3]

n, t = map(int, input().split())
songs = [[0, 0]]
for i in range(n):
    songs.append(list(map(int, input().split())))
print(solve(n, t, songs))

# Solution 2
def solve(n, t, songs):
    dp = [[[0] * 4 for _ in range(t + 1)] for _ in range(n + 1)]
    dp[0][0] = [1] * 4
    for i in range(1, n + 1):
        for j in range(t + 1):
            for k in range(1, 4):
                if j - songs[i][0] >= 0:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - songs[i][0]][k]
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
                if songs[i][1] == k:
                    dp[i][j][k] -= dp[i - 1][j - songs[i][0]][k]
    return dp[n][t][1] + dp[n][t][2] + dp[n][t][3]

n, t = map(int, input().split())
songs = [[0, 0]]
for i in range(n):
    songs.append(list(map(int, input().split())))
print(solve(n, t, songs))