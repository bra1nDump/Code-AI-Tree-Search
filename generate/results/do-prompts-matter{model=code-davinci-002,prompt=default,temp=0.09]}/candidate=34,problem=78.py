
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort(key=lambda x: x[0])
    # print(songs)
    dp = [[[0 for _ in range(T+1)] for _ in range(4)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, T+1):
            for k in range(1, 4):
                if j >= songs[i-1][0] and k != songs[i-1][1]:
                    dp[i][k][j] = dp[i-1][k][j] + dp[i-1][songs[i-1][1]][j-songs[i-1][0]]
                else:
                    dp[i][k][j] = dp[i-1][k][j]
    # print(dp)
    print(dp[n][1][T] + dp[n][2][T] + dp[n][3][T])

if True:
    main()