
#SOLUTION

n, T = map(int, input().split())

t = []
g = []
for i in range(n):
    t_i, g_i = map(int, input().split())
    t.append(t_i)
    g.append(g_i)

def modsum(a, b):
    return ((a % 1000000007) + (b % 1000000007)) % 1000000007

dp = [[0] * (T+1) for i in range(n)]

for i in range(n):
    if t[i] <= T:
        dp[i][t[i]] = 1

for i in range(1, n):
    for j in range(1, T+1):
        if g[i] != g[i-1]:
            dp[i][j] = modsum(dp[i][j], dp[i-1][j])
        if j >= t[i]:
            dp[i][j] = modsum(dp[i][j], dp[i-1][j-t[i]])

print(dp[n-1][T])