
import sys

def main():
    """
    The main function.
    """
    # Read input
    n, t = map(int, sys.stdin.readline().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))

    # Initialize the DP table
    dp = [[[0 for _ in range(t + 1)] for _ in range(4)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, 4):
            for k in range(1, t + 1):
                if songs[i - 1][0] > k:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - 1][k - songs[i - 1][0]]) % (10**9 + 7)

    # Print the answer
    print(dp[n][3][t])

if True:
    main()