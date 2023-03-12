
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])
    dp = [[0 for i in range(T+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, T+1):
            if j < songs[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
    ans = 0
    for i in range(n):
        ans += dp[i][T]
    print(ans)

if True:
    main()