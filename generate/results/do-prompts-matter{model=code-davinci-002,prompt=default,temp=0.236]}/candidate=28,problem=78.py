
# Solution

# This solution is based on dynamic programming.
# The idea is to use a 3D array dp[i][j][k] where i is the index of the song, j is the time left and k is the last genre played.
# dp[i][j][k] is the number of ways to play the first i songs with j time left and k as the last genre played.
# The base case is dp[0][T][0] = 1.
# The recurrence relation is dp[i][j][k] = sum(dp[i-1][j-t_i][g_i]) for all i, j, k.
# The answer is dp[n][0][0].

# This solution is O(n*T*3) = O(n*T) in time and O(n*T*3) = O(n*T) in space.

MOD = 10**9 + 7

n, T = map(int, input().split())

t = []
g = []

for i in range(n):
    t_i, g_i = map(int, input().split())
    t.append(t_i)
    g.append(g_i)

dp = [[[0 for k in range(4)] for j in range(T+1)] for i in range(n+1)]

dp[0][T][0] = 1

for i in range(1, n+1):
    for j in range(T+1):
        for k in range(1, 4):
            if j >= t[i-1]:
                dp[i][j][k] = dp[i-1][j-t[i-1]][g[i-1]]
            if k != g[i-1]:
                dp[i][j][k] += dp[i-1][j][k]
            dp[i][j][k] %= MOD

print(dp[n][0][0])