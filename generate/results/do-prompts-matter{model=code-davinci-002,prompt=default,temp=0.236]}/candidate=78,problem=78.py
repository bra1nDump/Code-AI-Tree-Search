
# solution

n, T = map(int, input().split())

t = [0] * n
g = [0] * n

for i in range(n):
    t[i], g[i] = map(int, input().split())

dp = [[[0 for i in range(T + 1)] for j in range(4)] for k in range(n + 1)]

dp[0][0][0] = 1

for i in range(1, n + 1):
    for j in range(1, 4):
        for k in range(T + 1):
            if k - t[i - 1] >= 0:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k - t[i - 1]]
            else:
                dp[i][j][k] = dp[i - 1][j][k]

print(dp[n][3][T])