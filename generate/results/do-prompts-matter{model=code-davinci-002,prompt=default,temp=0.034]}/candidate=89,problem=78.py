
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])
    dp = [[0 for i in range(T+1)] for j in range(n)]
    for i in range(n):
        for j in range(T+1):
            if i == 0:
                if j == songs[i][0]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                if j < songs[i][0]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
    print(dp)
    ans = 0
    for i in range(n):
        for j in range(T+1):
            if dp[i][j] == 0:
                continue
            for k in range(i+1, n):
                if songs[k][1] == songs[i][1]:
                    continue
                if j + songs[k][0] > T:
                    continue
                ans += dp[i][j] * dp[k][T-j-songs[k][0]]
    print(ans)

if True:
    main()