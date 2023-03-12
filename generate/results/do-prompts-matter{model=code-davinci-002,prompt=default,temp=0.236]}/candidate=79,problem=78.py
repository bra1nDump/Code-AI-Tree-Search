
import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    # print(songs)
    dp = [[0 for i in range(t + 1)] for j in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(t + 1):
            if j >= songs[i - 1][0]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    ans = 0
    for i in range(1, n + 1):
        ans += dp[i][t]
    print(ans)

if True:
    main()