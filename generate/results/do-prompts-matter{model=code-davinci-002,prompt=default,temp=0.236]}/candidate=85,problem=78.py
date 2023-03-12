
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    songs.sort()
    dp = [[[0] * (T + 1) for i in range(n)] for j in range(3)]
    for i in range(n):
        for j in range(T + 1):
            if songs[i][0] <= j:
                if songs[i][1] == 1:
                    dp[0][i][j] = dp[0][i - 1][j - songs[i][0]] + dp[1][i - 1][j - songs[i][0]] + dp[2][i - 1][j - songs[i][0]]
                elif songs[i][1] == 2:
                    dp[1][i][j] = dp[0][i - 1][j - songs[i][0]] + dp[1][i - 1][j - songs[i][0]] + dp[2][i - 1][j - songs[i][0]]
                elif songs[i][1] == 3:
                    dp[2][i][j] = dp[0][i - 1][j - songs[i][0]] + dp[1][i - 1][j - songs[i][0]] + dp[2][i - 1][j - songs[i][0]]
            else:
                dp[0][i][j] = dp[0][i - 1][j]
                dp[1][i][j] = dp[1][i - 1][j]
                dp[2][i][j] = dp[2][i - 1][j]
    print(dp[0][n - 1][T] + dp[1][n - 1][T] + dp[2][n - 1][T])

if True:
    main()