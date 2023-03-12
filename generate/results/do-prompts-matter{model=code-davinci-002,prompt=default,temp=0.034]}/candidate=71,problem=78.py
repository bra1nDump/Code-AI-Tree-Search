
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain time with a certain genre.
# The first dimension will be the time and the second dimension will be the genre.
# We will use the following recurrence relation to fill the array:
# dp[t][g] = dp[t-1][g] + dp[t-1][g-1] + dp[t-1][g+1]
# The first term is the number of ways to reach time t with genre g without using the current song.
# The second term is the number of ways to reach time t with genre g using the current song and the previous song having genre g-1.
# The third term is the number of ways to reach time t with genre g using the current song and the previous song having genre g+1.
# We will use the above recurrence relation to fill the array.
# The answer will be the sum of the last row of the array.

# Time complexity: O(n*T)
# Space complexity: O(T)

MOD = 10**9 + 7

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T+1)]
    dp[0][0] = 1
    for t in range(1, T+1):
        for g in range(1, 4):
            dp[t][g] = dp[t-1][g]
            if t-songs[g-1][0] >= 0:
                dp[t][g] += dp[t-songs[g-1][0]][songs[g-1][1]]
            if g > 1:
                dp[t][g] += dp[t-1][g-1]
            if g < 3:
                dp[t][g] += dp[t-1][g+1]
            dp[t][g] %= MOD
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    songs = [[0, 0] for _ in range(n)]
    for i in range(n):
        songs[i][0], songs[i][1] = map(int, input().split())
    print(solve(n, T, songs))