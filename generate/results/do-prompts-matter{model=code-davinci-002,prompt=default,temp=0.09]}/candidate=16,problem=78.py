
# Solution

# This solution is based on dynamic programming.
# Let's define $dp[i][j]$ as the number of ways to create a playlist of length $i$ with the last song having genre $j$.
# Then, we can calculate $dp[i][j]$ as the sum of $dp[i - t_k][k]$ for all $k$ such that $t_k \le i$ and $k \ne j$.
# The answer is the sum of $dp[T][j]$ for all $j$.

# Implementation

n, T = map(int, input().split())

t = [0] * n
g = [0] * n

for i in range(n):
    t[i], g[i] = map(int, input().split())

dp = [[0] * 4 for i in range(T + 1)]

for i in range(1, T + 1):
    for j in range(1, 4):
        for k in range(n):
            if t[k] <= i and g[k] != j:
                dp[i][j] += dp[i - t[k]][g[k]]

ans = 0
for i in range(1, 4):
    ans += dp[T][i]

print(ans % (10 ** 9 + 7))