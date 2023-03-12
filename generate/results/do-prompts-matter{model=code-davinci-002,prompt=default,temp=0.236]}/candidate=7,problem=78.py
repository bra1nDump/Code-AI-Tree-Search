
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    # print(songs)
    # print(n, T)
    # print(songs)

    # dp[i][j] = number of ways to make a playlist of length j using songs 0 to i
    # dp[i][j] = sum(dp[i-1][j-t]) for all songs i with t <= j
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ...
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ... + dp[i-1][j-t-t] - dp[i-1][j-t-t-1]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ... + dp[i-1][j-t-t] - dp[i-1][j-t-t-1] + dp[i-1][j-t-t-2] - dp[i-1][j-t-t-3] + ...
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ... + dp[i-1][j-t-t] - dp[i-1][j-t-t-1] + dp[i-1][j-t-t-2] - dp[i-1][j-t-t-3] + ... + dp[i-1][j-t-t-t] - dp[i-1][j-t-t-t-1]
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ... + dp[i-1][j-t-t] - dp[i-1][j-t-t-1] + dp[i-1][j-t-t-2] - dp[i-1][j-t-t-3] + ... + dp[i-1][j-t-t-t] - dp[i-1][j-t-t-t-1] + dp[i-1][j-t-t-t-2] - dp[i-1][j-t-t-t-3] + ...
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-1][j-t-1] + dp[i-1][j-t-2] - dp[i-1][j-t-3] + ... + dp[i-1][j-t-t] - dp[i-1][j-t-t-1] + dp[i-1][j-t-t-2]