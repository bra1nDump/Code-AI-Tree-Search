
# Solution 1
"""
n, t = map(int, input().split())
songs = []
for i in range(n):
    t_i, g_i = map(int, input().split())
    songs.append((t_i, g_i))

# dp[i][j] = number of ways to construct playlist with total duration j using songs up to (and including) i
dp = [[0] * (t + 1) for i in range(n)]
dp[0][songs[0][0]] = 1
for i in range(1, n):
    for j in range(1, t + 1):
        dp[i][j] = dp[i - 1][j]
        if j - songs[i][0] >= 0 and dp[i - 1][j - songs[i][0]] != 0:
            dp[i][j] += dp[i - 1][j - songs[i][0]]
            if songs[i][1] == songs[i - 1][1]:
                dp[i][j] -= dp[i - 1][j - songs[i][0]]

print(dp[n - 1][t])
"""

# Solution 2
"""
n, t = map(int, input().split())
songs = []
for i in range(n):
    t_i, g_i = map(int, input().split())
    songs.append((t_i, g_i))

# dp[i][j][k] = number of ways to construct playlist with total duration j using songs up to (and including) i,
# where k is the last song's genre
dp = [[[0] * 4 for j in range(t + 1)] for i in range(n)]
for i in range(1, 4):
    dp[0][songs[0][0]][i] = 1
for i in range(1, n):
    for j in range(1, t + 1):
        for k in range(1, 4):
            dp[i][j][k] = dp[i - 1][j][k]
            if j - songs[i][0] >= 0 and dp[i - 1][j - songs[i][0]][k] != 0:
                dp[i][j][songs[i][1]] += dp[i - 1][j - songs[i][0]][k]

print(dp[n - 1][t][1] + dp[n - 1][t][2] + dp[n - 1][t][3])
"""

# Solution 3
"""
n, t = map(int, input().split())
songs = []
for i in range(n):
    t_i, g_i = map(int, input().split())
    songs.append((t_i, g_i))

# dp[i][j] = number of ways to construct playlist with total duration j using songs up to (and including) i
dp = [[0] * (t + 1) for i in range(n)]
dp[0][songs[0][0]] = 1
for i in range(1, n):
    for j in range(1, t + 1):
        dp[i][j] = dp[i - 1][j]
        if j - songs[i][0] >= 0 and dp[i - 1][j - songs[i][0]] != 0:
            dp[i][j] += dp[i - 1][j - songs[i][0]]

print(dp[n - 1][t])
"""

# Solution 4
"""
n, t = map(int, input().split())
songs = []
for i in range(n):
    t_i, g_i = map(int, input().split())
    songs.append((t_i, g_i))

# dp[i][j] = number of ways to construct playlist with total duration j using songs up to (and including) i
dp = [[0] * (t + 1) for i in range(n)]
dp[0][songs[0][0]] = 1
for i in range(1, n):
    for j in range(1, t + 1):
        dp[i][j] = dp[i - 1][j]