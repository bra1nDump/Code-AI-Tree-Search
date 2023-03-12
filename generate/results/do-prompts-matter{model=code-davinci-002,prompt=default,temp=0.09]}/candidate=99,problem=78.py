
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of playlists that can be made with the first i songs and a total duration of j.
# We will use the following recurrence relation to fill the array:
# dp[i][j] = sum(dp[i-1][j-k]) for all k such that j-k >= 0 and k != t[i]
# The base case is dp[0][0] = 1
# The answer is dp[n][T]

# Time complexity: O(n*T)
# Space complexity: O(n*T)

MOD = 10**9 + 7

def solve(n, T, t, g):
    dp = [[0 for _ in range(T+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            for k in range(j+1):
                if k != t[i-1]:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    return dp[n][T]

n, T = map(int, input().split())
t = []
g = []
for _ in range(n):
    ti, gi = map(int, input().split())
    t.append(ti)
    g.append(gi)
print(solve(n, T, t, g))