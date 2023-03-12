
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        songs.append((t, g))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j] = number of ways to play songs[0:i] with total time j
    dp = [[0 for j in range(T+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        t, g = songs[i-1]
        for j in range(T+1):
            if j >= t:
                dp[i][j] = dp[i-1][j-t]
            if i >= 2 and j >= t and songs[i-2][1] != g:
                dp[i][j] += dp[i-2][j-t]
    return dp[n][T]

if True:
    main()