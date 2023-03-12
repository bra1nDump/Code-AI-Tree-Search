
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])
    #print(songs)
    #print(T)
    #print(n)
    #print(songs)
    dp = [[0 for i in range(T+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            if j >= songs[i-1][0]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i-1][0]]
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    ans = dp[n][T]
    #print(ans)
    for i in range(1, n+1):
        for j in range(1, T+1):
            if songs[i-1][1] == songs[i-2][1]:
                ans -= dp[i-1][j-songs[i-1][0]]
    print(ans)

if True:
    main()