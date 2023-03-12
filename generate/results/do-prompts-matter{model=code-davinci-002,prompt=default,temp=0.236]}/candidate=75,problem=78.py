
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j] = number of ways to create a playlist of length i using songs 1..j
    # dp[i][j] = sum(dp[i-t][k]) for k in range(j) if songs[k][1] != songs[j][1]
    # dp[i][j] = 0 if i < 0 or i < songs[j][0]
    # dp[i][j] = 1 if i == songs[j][0]
    # dp[0][j] = 1 for all j
    # dp[i][0] = 0 for all i > songs[0][0]
    # dp[i][0] = 1 for all i <= songs[0][0]
    # dp[i][j] = dp[i][j-1] + dp[i-songs[j][0]][j-1] - dp[i-songs[j][0]-1][j-1]
    # dp[i][j] = dp[i][j-1] + dp[i-songs[j][0]][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] if i < songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = 0 if i < 0
    # dp[i][j] = dp[i][j-1] if i >= 0
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = 0 if i < 0
    # dp[i][j] = dp[i][j-1] if i >= 0
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] if i < songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] if i < songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] if i < songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] - dp[i-songs[j][0]-1][j-1] if i >= songs[j][0]
    # dp[i][j] = dp[i][j-1] if i < songs[j][0]