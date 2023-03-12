
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        t, g = map(int, sys.stdin.readline().split())
        songs.append((t, g))
    # print(songs)
    # print(n, T)
    MOD = 10**9 + 7
    dp = [[0 for _ in range(T+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, T+1):
            if j >= songs[i-1][0]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-songs[i-1][0]]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    ans = dp[n][T]
    for i in range(1, n+1):
        for j in range(1, T+1):
            if j >= songs[i-1][0]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-songs[i-1][0]]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
            if songs[i-1][1] == songs[i-2][1]:
                ans = (ans - dp[i][j]) % MOD
    print(ans)

if True:
    main()