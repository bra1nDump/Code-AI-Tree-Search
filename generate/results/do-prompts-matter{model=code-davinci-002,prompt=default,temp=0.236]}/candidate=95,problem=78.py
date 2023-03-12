
# Solution 1
def solve(n, T, songs):
    """
    >>> solve(3, 3, [(1, 1), (1, 2), (1, 3)])
    6
    >>> solve(3, 3, [(1, 1), (1, 1), (1, 3)])
    2
    >>> solve(4, 10, [(5, 3), (2, 1), (3, 2), (5, 1)])
    10
    """
    MOD = 10**9 + 7
    # dp[i][j] is the number of ways to make a playlist of length i with the last song being genre j
    dp = [[0 for j in range(4)] for i in range(T+1)]
    dp[0][0] = 1
    for i in range(1, T+1):
        for j in range(1, 4):
            for song in songs:
                if song[0] <= i and song[1] != j:
                    dp[i][song[1]] += dp[i-song[0]][j]
                    dp[i][song[1]] %= MOD
    return sum(dp[T]) % MOD

# Solution 2
def solve(n, T, songs):
    """
    >>> solve(3, 3, [(1, 1), (1, 2), (1, 3)])
    6
    >>> solve(3, 3, [(1, 1), (1, 1), (1, 3)])
    2
    >>> solve(4, 10, [(5, 3), (2, 1), (3, 2), (5, 1)])
    10
    """
    MOD = 10**9 + 7
    # dp[i][j] is the number of ways to make a playlist of length i with the last song being genre j
    dp = [[0 for j in range(4)] for i in range(T+1)]
    dp[0][0] = 1
    for i in range(1, T+1):
        for j in range(1, 4):
            for song in songs:
                if song[0] <= i and song[1] != j:
                    dp[i][song[1]] += dp[i-song[0]][j]
                    dp[i][song[1]] %= MOD
    return sum(dp[T]) % MOD

if True:
    n, T = [int(x) for x in input().split()]
    songs = []
    for i in range(n):
        t, g = [int(x) for x in input().split()]
        songs.append((t, g))
    print(solve(n, T, songs))