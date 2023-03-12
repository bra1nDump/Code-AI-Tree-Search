
# Solution 1

import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    durations = []
    genres = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        durations.append(t)
        genres.append(g)
    dp = [[[0 for k in range(T+1)] for j in range(4)] for i in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(1, 4):
            for k in range(T+1):
                if k >= durations[i-1]:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-durations[i-1]]
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    print(dp[n][3][T])

if True:
    main()