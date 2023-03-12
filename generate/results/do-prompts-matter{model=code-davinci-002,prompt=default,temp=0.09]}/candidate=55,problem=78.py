
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain time with a certain genre.
# We will use the following notation:
# dp[i][j] = number of ways to reach time i with genre j
# We will use the following recurrence relation:
# dp[i][j] = sum(dp[i - t_k][k]) for all k != j
# We will use the following base cases:
# dp[0][j] = 1 for all j
# dp[i][j] = 0 for all i < 0
# dp[i][j] = 0 for all j < 0
# dp[i][j] = 0 for all j > 3
# dp[i][j] = 0 for all i > T
# We will use the following answer:
# sum(dp[T][j]) for all j

# Time complexity: O(n * T)
# Space complexity: O(n * T)

# Importing standard libraries
import sys

# Parsing the input
n, T = map(int, sys.stdin.readline().split())
t = []
g = []
for i in range(n):
    t_i, g_i = map(int, sys.stdin.readline().split())
    t.append(t_i)
    g.append(g_i)

# Defining the modulus
MOD = 10**9 + 7

# Defining the dp array
dp = [[0 for j in range(4)] for i in range(T + 1)]

# Defining the base cases
for j in range(4):
    dp[0][j] = 1

# Defining the recurrence relation
for i in range(1, T + 1):
    for j in range(4):
        for k in range(n):
            if g[k] != j and i - t[k] >= 0:
                dp[i][j] += dp[i - t[k]][g[k]]
                dp[i][j] %= MOD

# Defining the answer
ans = 0
for j in range(4):
    ans += dp[T][j]
    ans %= MOD

# Printing the answer
print(ans)