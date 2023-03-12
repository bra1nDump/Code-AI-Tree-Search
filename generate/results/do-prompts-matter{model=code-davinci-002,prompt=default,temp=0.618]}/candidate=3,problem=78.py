
"""
    This solution is inspired by the solution of "C. Way to Home" problem.
    The idea is to find the number of ways to sort a list of integers such that
    they are in ascending order, and there are no two consecutive integers 
    with the same value.
"""

"""
    This solution is inspired by the solution of "C. Way to Home" problem.
    The idea is to find the number of ways to sort a list of integers such that
    they are in ascending order, and there are no two consecutive integers 
    with the same value.
"""

"""
    This solution is inspired by the solution of "C. Way to Home" problem.
    The idea is to find the number of ways to sort a list of integers such that
    they are in ascending order, and there are no two consecutive integers 
    with the same value.
"""

"""
    This solution is inspired by the solution of "C. Way to Home" problem.
    The idea is to find the number of ways to sort a list of integers such that
    they are in ascending order, and there are no two consecutive integers 
    with the same value.
"""

"""
    This solution is inspired by the solution of "C. Way to Home" problem.
    The idea is to find the number of ways to sort a list of integers such that
    they are in ascending order, and there are no two consecutive integers 
    with the same value.
"""

if True:
    n, T = [int(x) for x in input().split()]
    songs = [[int(x) for x in input().split()] for i in range(n)]
    mod = 1000000007
    # dp[i][j][k] denotes the number of ways to sort the first i songs such that
    # the sum of their durations is j and the last genre is k.
    dp = [[[0 for k in range(4)] for j in range(T + 1)] for i in range(n + 1)]
    # Base cases
    for i in range(1, n + 1):
        dp[i][0][0] = 1
    for j in range(1, T + 1):
        dp[0][j][0] = 0
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            for k in range(1, 4):
                if j >= songs[i - 1][0]:
                    dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - songs[i - 1][0]][songs[i - 1][1]]) % mod
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
    print(dp[n][T][0])