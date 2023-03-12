
def solve(n, T, g, t):
    dp = [ [0]*(T+1) for _ in range(n+1) ]
    MOD = 1000000007
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, T+1):
            if j < t[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                if i > 1 and g[i-1] != g[i-2]:
                    dp[i][j] += dp[i-1][j-t[i-1]]
                elif i == 1:
                    dp[i][j] += dp[i-1][j-t[i-1]]
    return dp[n][T]

n, T = map(int, input().split())
g = [0]
t = []
for _ in range(n):
    t_i, g_i = map(int, input().split())
    t.append(t_i)
    g.append(g_i)
print(solve(n, T, g, t))