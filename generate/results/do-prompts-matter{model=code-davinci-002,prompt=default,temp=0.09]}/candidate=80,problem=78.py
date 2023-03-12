
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j][k] = number of ways to play songs 0..i with total time j and last song genre k
    dp = [[[0 for k in range(4)] for j in range(T+1)] for i in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            for k in range(4):
                if j >= songs[i-1][0]:
                    dp[i][j][songs[i-1][1]] += dp[i-1][j-songs[i-1][0]][k]
                if k != songs[i-1][1]:
                    dp[i][j][k] += dp[i-1][j][k]
    return sum(dp[n][T])

if True:
    main()