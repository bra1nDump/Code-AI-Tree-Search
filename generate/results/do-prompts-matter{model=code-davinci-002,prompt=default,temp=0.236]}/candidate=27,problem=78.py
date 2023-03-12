
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    dp = [[0 for i in range(T + 1)] for j in range(n)]
    dp[0][0] = 1
    dp[0][songs[0][0]] = 1
    for i in range(1, n):
        for j in range(T + 1):
            if dp[i - 1][j] > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % 1000000007
                if j + songs[i][0] <= T:
                    dp[i][j + songs[i][0]] = (dp[i][j + songs[i][0]] + dp[i - 1][j]) % 1000000007
    ans = 0
    for i in range(n):
        if songs[i][1] == songs[0][1]:
            ans = (ans + dp[i][T]) % 1000000007
    print(ans)

if True:
    main()