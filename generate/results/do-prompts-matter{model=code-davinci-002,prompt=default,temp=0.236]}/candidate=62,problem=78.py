
# SOLUTION
# This is a dynamic programming problem.
# Let's define a state as a tuple (i, j, k), where
# i is the index of the song,
# j is the time left,
# k is the genre of the last song.
# We can use a 3D array to store the number of ways to reach a state.
# The base case is when i = n and j = 0.
# The recurrence relation is:
# dp[i][j][k] = dp[i + 1][j][1] + dp[i + 1][j][2] + dp[i + 1][j][3]
# if t[i] > j
# dp[i][j][k] = dp[i + 1][j][1] + dp[i + 1][j][2] + dp[i + 1][j][3]
# if k == g[i]
# dp[i][j][k] = dp[i + 1][j - t[i]][g[i]]
# otherwise

MOD = 10**9 + 7

def solve(n, t, g, T):
    dp = [[[0 for _ in range(4)] for _ in range(T + 1)] for _ in range(n + 1)]
    dp[n][0][0] = 1
    for i in range(n - 1, -1, -1):
        for j in range(T + 1):
            for k in range(1, 4):
                if t[i] > j:
                    dp[i][j][k] = dp[i + 1][j][1] + dp[i + 1][j][2] + dp[i + 1][j][3]
                elif k == g[i]:
                    dp[i][j][k] = dp[i + 1][j][1] + dp[i + 1][j][2] + dp[i + 1][j][3]
                else:
                    dp[i][j][k] = dp[i + 1][j - t[i]][g[i]]
                dp[i][j][k] %= MOD
    return dp[0][T][0]

if True:
    n, T = map(int, input().split())
    t = [0] * n
    g = [0] * n
    for i in range(n):
        t[i], g[i] = map(int, input().split())
    print(solve(n, t, g, T))