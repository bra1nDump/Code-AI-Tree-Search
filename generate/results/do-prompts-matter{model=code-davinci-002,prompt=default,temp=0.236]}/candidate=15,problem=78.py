
# Solution

# This solution is based on dynamic programming.
# Let dp[i][j][k] be the number of ways to choose a playlist of length i,
# where the last song has genre j and the second to last song has genre k.
# Then, we can calculate dp[i][j][k] by summing over all the ways to choose
# a playlist of length i-1, where the last song has genre k and the second to
# last song has genre l.

# The base cases are dp[0][0][0] = 1 and dp[0][j][k] = 0 for all other j and k.

# The answer is the sum of dp[T][j][k] over all j and k.

# Time complexity: O(n*T*3^2)
# Space complexity: O(n*T*3^2)

#!/usr/bin/env python3

n, T = map(int, input().split())

# dp[i][j][k] is the number of ways to choose a playlist of length i,
# where the last song has genre j and the second to last song has genre k.
dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(T + 1)]

# Base cases
dp[0][0][0] = 1

for i in range(1, T + 1):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                if j == k:
                    continue
                dp[i][j][k] += dp[i - 1][k][l]

# The answer is the sum of dp[T][j][k] over all j and k.
answer = 0
for j in range(1, 4):
    for k in range(1, 4):
        answer += dp[T][j][k]

print(answer)