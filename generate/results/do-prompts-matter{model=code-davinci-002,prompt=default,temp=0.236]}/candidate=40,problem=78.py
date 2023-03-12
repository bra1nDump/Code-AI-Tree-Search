
# Solution

# This solution is based on dynamic programming.
# Let's define $dp[i][j]$ as the number of different sequences of songs, the total length of exactly $i$ minutes, such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different.
# Then, we can write the following recurrence relation:
# $dp[i][j] = \sum_{k=1}^n dp[i - t_k][j - g_k]$
# where $t_k$ and $g_k$ are the duration and genre of the $k$-th song, respectively.
# The base case is $dp[0][0] = 1$.
# The answer is $dp[T][3]$.

# Implementation

# The following implementation is based on the above recurrence relation.
# The time complexity is $O(nT)$.
# The space complexity is $O(nT)$.

#!/usr/bin/env python3

def solve(n, T, t, g):
    dp = [[0] * (3 + 1) for _ in range(T + 1)]
    dp[0][0] = 1
    for i in range(1, T + 1):
        for j in range(1, 3 + 1):
            for k in range(n):
                if i >= t[k] and j >= g[k]:
                    dp[i][j] += dp[i - t[k]][j - g[k]]
    return dp[T][3]

def main():
    n, T = map(int, input().split())
    t = []
    g = []
    for _ in range(n):
        ti, gi = map(int, input().split())
        t.append(ti)
        g.append(gi)
    print(solve(n, T, t, g))

if True:
    main()