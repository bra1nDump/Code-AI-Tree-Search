
#------------------------------------------------------------------------------#

def solve_easy(n, T, t, g):
    """
    >>> solve_easy(3, 3, [1, 1, 1], [1, 2, 3])
    6
    >>> solve_easy(3, 3, [1, 1, 1], [1, 1, 3])
    2
    >>> solve_easy(4, 10, [5, 2, 3, 5], [3, 1, 2, 1])
    10
    """
    # dp[i][j][k] = number of ways to make a playlist of length i, ending with
    #               song j, and the genre of the previous song was k
    dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(T + 1)]
    dp[0][0][0] = 1
    for i in range(1, T + 1):
        for j in range(1, n + 1):
            for k in range(1, 4):
                if i - t[j - 1] < 0:
                    continue
                if k == g[j - 1]:
                    dp[i][j][k] = dp[i - t[j - 1]][j - 1][k]
                else:
                    dp[i][j][k] = sum(dp[i - t[j - 1]][j - 1])
    return sum(dp[T][n])

#------------------------------------------------------------------------------#

def solve_hard(n, T, t, g):
    """
    >>> solve_hard(3, 3, [1, 1, 1], [1, 2, 3])
    6
    >>> solve_hard(3, 3, [1, 1, 1], [1, 1, 3])
    2
    >>> solve_hard(4, 10, [5, 2, 3, 5], [3, 1, 2, 1])
    10
    """
    # dp[i][j][k] = number of ways to make a playlist of length i, ending with
    #               song j, and the genre of the previous song was k
    dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(T + 1)]
    dp[0][0][0] = 1
    for i in range(1, T + 1):
        for j in range(1, n + 1):
            for k in range(1, 4):
                if i - t[j - 1] < 0:
                    continue
                if k == g[j - 1]:
                    dp[i][j][k] = dp[i - t[j - 1]][j - 1][k]
                else:
                    dp[i][j][k] = sum(dp[i - t[j - 1]][j - 1])
    return sum(dp[T][n])

#------------------------------------------------------------------------------#

def main():
    n, T = map(int, input().split())
    t = []
    g = []
    for _ in range(n):
        ti, gi = map(int, input().split())
        t.append(ti)
        g.append(gi)
    print(solve_easy(n, T, t, g))

#------------------------------------------------------------------------------#

if True:
    main()