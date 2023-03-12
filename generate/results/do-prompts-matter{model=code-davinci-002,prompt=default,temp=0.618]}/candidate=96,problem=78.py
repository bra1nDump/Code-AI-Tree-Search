
import sys

def get_num_playlists(n, t):
    """
    n -- number of songs
    t -- total time in minutes
    """
    dp = [[[0 for _ in range(0, 3)] for _ in range(0, 16)] for _ in range(0, 226)]
    for i in range(0, n + 1):
        dp[0][i][0] = 1
    for i in range(1, t + 1):
        for j in range(1, n + 1):
            for k in range(0, 3):
                for l in range(1, 16):
                    if k == 0:
                        dp[i][j][k] += dp[i - l][j - 1][k]
                    else:
                        dp[i][j][k] += dp[i - l][j - 1][k - 1]
    return dp[t][n][2]

def main():
    sys.stdin = open('input.txt', 'r')
    n, t = map(int, input().split(' '))
    print(get_num_playlists(n, t))

if True:
    main()