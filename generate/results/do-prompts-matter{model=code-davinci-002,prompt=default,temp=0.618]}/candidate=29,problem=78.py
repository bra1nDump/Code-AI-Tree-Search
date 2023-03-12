
# Solution
def solve(n, t, songs):
    """
    >>> solve(3, 3, [{'t': 1, 'g': 1}, {'t': 1, 'g': 2}, {'t': 1, 'g': 3}])
    6
    >>> solve(3, 3, [{'t': 1, 'g': 1}, {'t': 1, 'g': 1}, {'t': 1, 'g': 3}])
    2
    >>> solve(4, 10, [{'t': 5, 'g': 3}, {'t': 2, 'g': 1}, {'t': 3, 'g': 2}, {'t': 5, 'g': 1}])
    10
    """
    MOD = 10**9 + 7

    # Count the number of ways to reach sum `t` using the first `i` songs,
    # the last song played is `j`.
    dp = [[[0 for _ in range(n)] for _ in range(t + 1)] for _ in range(n + 1)]

    # Base case:
    # dp[i][0][i] = 1 for all `i`
    for i in range(n + 1):
        dp[i][0][i] = 1

    for i in range(1, n + 1):
        for j in range(n):
            for k in range(t + 1):
                if songs[j]['t'] <= k:
                    for l in range(n):
                        if songs[j]['g'] != songs[l]['g']:
                            dp[i][k][j] += dp[i - 1][k - songs[j]['t']][l]
                            dp[i][k][j] %= MOD

    return sum(dp[n][t]) % MOD


if True:
    n, t = map(int, input().split())
    songs = []
    for _ in range(n):
        t_i, g_i = map(int, input().split())
        songs.append({'t': t_i, 'g': g_i})

    print(solve(n, t, songs))