
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    dp = [[[0 for _ in range(T+1)] for _ in range(4)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 4):
            for k in range(1, T+1):
                if songs[i-1][0] <= k and songs[i-1][1] == j:
                    dp[i][j][k] = dp[i-1][j][k-songs[i-1][0]] + dp[i-1][j-1][k-songs[i-1][0]]
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    return dp[n][3][T]

if True:
    main()