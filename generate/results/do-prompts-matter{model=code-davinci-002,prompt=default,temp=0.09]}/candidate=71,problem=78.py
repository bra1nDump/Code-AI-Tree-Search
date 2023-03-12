
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of possible playlists for each duration and genre.
# The first dimension will be the duration and the second dimension will be the genre.
# We will use the following recurrence relation to fill the array:
# dp[i][j] = sum(dp[i - t][k]) for all k != j
# where i is the duration, j is the genre, t is the duration of the song, and k is the genre of the song.
# The base case is when i = 0, in which case dp[0][j] = 1 for all j.
# The answer will be the sum of all dp[T][j] for all j.

# Time complexity: O(n * T * g)
# Space complexity: O(n * T)

MOD = 10**9 + 7

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    for j in range(1, 4):
        dp[0][j] = 1
    for i in range(1, T + 1):
        for j in range(1, 4):
            for t, k in songs:
                if i - t >= 0 and k != j:
                    dp[i][j] += dp[i - t][k]
                    dp[i][j] %= MOD
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    print(solve(n, T, songs))