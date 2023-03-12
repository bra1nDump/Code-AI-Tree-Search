
#!/usr/bin/env python3

import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    songs.sort()
    dp = [[0 for _ in range(T+1)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= songs[i][0] and dp[i-1][j-songs[i][0]] != 0:
                dp[i][j] += dp[i-1][j-songs[i][0]]
    ans = 0
    for i in range(T+1):
        ans += dp[n-1][i]
    print(ans)

if True:
    main()