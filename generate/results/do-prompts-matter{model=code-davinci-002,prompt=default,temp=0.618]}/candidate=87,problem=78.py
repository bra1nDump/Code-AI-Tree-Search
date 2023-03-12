


def find_paths(n, T, dp):  # dp[n][T] = dp[n-1][T-ti] + dp[n-1][T]-ti
    if dp[n][T] != -1:
        return dp[n][T]
    if n == 0 and T > 0:
        return 0
    if T == 0:
        return 1
    if n > 0 and T >= 0:
        dp[n][T] = find_paths(n - 1, T, dp) + find_paths(n, T - 1, dp)
    return dp[n][T]


def find_ways(n, T, t, dp):
    if dp[n][T] != -1:
        return dp[n][T]
    if n == 0 and T > 0:
        return 0
    if T == 0:
        return 1
    if n > 0 and T > 0:
        dp[n][T] = find_paths(n - 1, T, dp)
        if T >= t[n]:
            dp[n][T] -= find_paths(n - 1, T - t[n], dp)
    return dp[n][T]


def find_songs(n, T, t, g, dp):
    if dp[n][T] != -1:
        return dp[n][T]
    if n == 0 and T > 0:
        return 0
    if T == 0:
        return 1
    if n > 0 and T > 0:
        if g[n] != g[n - 1]:
            dp[n][T] = find_ways(n - 1, T, t, dp)
        if T >= t[n]:
            if g[n] != g[n - 1]:
                dp[n][T] += find_ways(n - 1, T - t[n], t, dp)
            else:
                dp[n][T] = find_ways(n - 1, T - t[n], t, dp)
    return dp[n][T]


def find_ans(n, T, t, g, dp):
    if dp[n][T] != -1:
        return dp[n][T]
    if n == 0 and T > 0:
        return 0
    if T == 0:
        return 1
    if n > 0 and T > 0:
        dp[n][T] = find_songs(n - 1, T, t, g, dp)
        if T >= t[n]:
            dp[n][T] += find_songs(n - 1, T - t[n], t, g, dp)
    return dp[n][T]


def main():
    n, T = map(int, input().split())
    t = [0 for _ in range(n + 1)]
    g = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        t[i], g[i] = map(int, input().split())
    dp = [[-1 for _ in range(T + 1)] for _ in range(n + 1)]
    print(find_ans(n, T, t, g, dp))


if True:
    main()