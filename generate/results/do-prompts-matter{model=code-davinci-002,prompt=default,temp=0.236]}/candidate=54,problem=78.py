
import sys

def solve(n, T, songs):
    # dp[i][j][k] = number of ways to make a playlist of length i ending with song j and genre k
    dp = [[[0 for _ in range(4)] for _ in range(n+1)] for _ in range(T+1)]
    dp[0][0][0] = 1
    for i in range(1, T+1):
        for j in range(1, n+1):
            for k in range(1, 4):
                if songs[j-1][0] <= i:
                    dp[i][j][k] = dp[i-songs[j-1][0]][j-1][k]
                    if songs[j-1][1] != k:
                        dp[i][j][k] += dp[i-songs[j-1][0]][j-1][songs[j-1][1]]
    return sum(dp[T][n]) % 1000000007

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

if True:
    main()