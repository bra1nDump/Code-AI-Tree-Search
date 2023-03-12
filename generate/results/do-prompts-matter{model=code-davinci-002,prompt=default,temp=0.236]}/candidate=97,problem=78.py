
import sys

def main():
    """
    This is the main function.
    """
    # Read the input
    n, t = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))

    # Create the DP table
    dp = [[[0 for _ in range(t+1)] for _ in range(4)] for _ in range(n+1)]

    # Initialize the DP table
    for i in range(1, n+1):
        dp[i][0][0] = 1

    # Populate the DP table
    for i in range(1, n+1):
        for j in range(1, 4):
            for k in range(1, t+1):
                if k >= songs[i-1][0] and j != songs[i-1][1]:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][songs[i-1][1]][k-songs[i-1][0]]
                else:
                    dp[i][j][k] = dp[i-1][j][k]

    # Print the answer
    print(dp[n][0][t])

if True:
    main()