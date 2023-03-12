
# SOLUTION
# This is a dynamic programming problem.
# Let's define $dp[i][j]$ as the number of ways to create a playlist of length $i$ with the last song of genre $j$.
# We can iterate over all possible lengths of the playlist and all possible genres of the last song.
# For each of them, we can iterate over all possible genres of the previous song and add the number of ways to create a playlist of length $i - 1$ with the last song of genre $prev$ to $dp[i][j]$.
# We should also add the number of ways to create a playlist of length $i - 1$ with the last song of genre $j$ to $dp[i][j]$.
# The answer is the sum of all $dp[T][j]$ for all possible genres $j$.
# Time complexity: $O(nT)$.
# Memory complexity: $O(T)$.

MOD = 10**9 + 7

def solve(n, T, songs):
    dp = [[0] * 4 for _ in range(T + 1)]
    for i in range(1, T + 1):
        for j in range(1, 4):
            for prev in range(1, 4):
                if prev != j:
                    dp[i][j] += dp[i - 1][prev]
            dp[i][j] += dp[i - 1][j]
            for t, g in songs:
                if i >= t and g == j:
                    dp[i][j] += 1
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    songs = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, T, songs))