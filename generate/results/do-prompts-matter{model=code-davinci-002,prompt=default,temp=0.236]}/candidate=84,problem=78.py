
# SOLUTION
# The problem is to find the number of ways to arrange the songs such that there are no two consecutive songs of the same genre.
# This is a dynamic programming problem.
# Let dp[i][j] be the number of ways to arrange the songs such that the last song is of genre j and the total duration is i.
# Then, dp[i][j] = sum(dp[i - t_k][k]) for all k != j.
# The answer is sum(dp[T][j]) for all j.

MOD = 10**9 + 7

def solve(n, T, t, g):
    dp = [[0] * 4 for _ in range(T + 1)]
    for i in range(1, T + 1):
        for j in range(1, 4):
            for k in range(1, n + 1):
                if g[k] != j and i >= t[k]:
                    dp[i][j] += dp[i - t[k]][g[k]]
                    dp[i][j] %= MOD
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    t = [0]
    g = [0]
    for _ in range(n):
        t_i, g_i = map(int, input().split())
        t.append(t_i)
        g.append(g_i)
    print(solve(n, T, t, g))