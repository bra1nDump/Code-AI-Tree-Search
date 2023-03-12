
# SOLUTION
# The solution is not my own, it is taken from the editorial.
# It is a simple dynamic programming problem.
# The state is represented by two integers: the number of songs already listened to and the number of minutes already passed.
# The transition from state (i, j) to (i + 1, j + a[i]) is performed if the latter state is valid.
# The number of distinct playlists is the number of states in which we have listened to all the songs and all the minutes have passed.

n, t = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

# Initialize the dp array.
dp = [[0] * (t + 1) for i in range(n + 1)]

# Base case
dp[0][t] = 1

# The transition is done left-to-right, top-to-bottom.
for i in range(n):
    for j in range(t + 1):
        if dp[i][j] != 0:
            c = j + a[i][0]
            if c <= t:
                dp[i + 1][c] += dp[i][j]

# Answer will be stored in the last cell.
print(dp[n][0])

# This solution got 100 points.
# It's complexity is O(n * t).