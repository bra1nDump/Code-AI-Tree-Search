
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))

    # dp[i][j][k] = number of ways to get to time i with last genre j and last song k
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs[l][1] != j
    # dp[i][j][k] = sum(dp[i-t][j][l]) for all l != k and songs