
import sys

def main():
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])
    songs.sort()
    dp = [[0 for i in range(T+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= songs[i-1][0]:
                dp[i][j] += dp[i-1][j-songs[i-1][0]]
    ans = dp[n][T]
    for i in range(1, n+1):
        for j in range(1, T+1):
            if songs[i-1][1] == songs[i-2][1]:
                ans -= dp[i-1][j-songs[i-1][0]]
    print(ans)

if True:
    main()