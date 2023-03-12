
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(tuple(map(int, sys.stdin.readline().split())))
    songs.sort()
    dp = [[[0 for _ in range(T+1)] for _ in range(4)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(T+1):
                if dp[i][j][k] == 0:
                    continue
                for l in range(j, 4):
                    if k + songs[i][0] <= T:
                        dp[i+1][l][k+songs[i][0]] += dp[i][j][k]
    print(sum(dp[n][j][T] for j in range(4)))

if True:
    main()