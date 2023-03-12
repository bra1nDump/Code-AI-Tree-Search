
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))

    # dp[i][j] = number of ways to make a playlist of length j using the first i songs
    dp = [[0 for j in range(T+1)] for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            # if we can't use the ith song, then the number of ways to make a playlist of length j is the same as the number of ways to make a playlist of length j using the first i-1 songs
            if j < songs[i-1][0]:
                dp[i][j] = dp[i-1][j]
            # if we can use the ith song, then the number of ways to make a playlist of length j is the sum of the number of ways to make a playlist of length j using the first i-1 songs and the number of ways to make a playlist of length j-t_i using the first i-1 songs
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i-1][0]]

    # print(dp)

    # dp2[i][j] = number of ways to make a playlist of length j using the first i songs such that the last two songs are not of the same genre
    dp2 = [[0 for j in range(T+1)] for i in range(n+1)]
    dp2[0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            # if we can't use the ith song, then the number of ways to make a playlist of length j such that the last two songs are not of the same genre is the same as the number of ways to make a playlist of length j using the first i-1 songs such that the last two songs are not of the same genre
            if j < songs[i-1][0]:
                dp2[i][j] = dp2[i-1][j]
            # if we can use the ith song, then the number of ways to make a playlist of length j such that the last two songs are not of the same genre is the sum of the number of ways to make a playlist of length j using the first i-1 songs such that the last two songs are not of the same genre and the number of ways to make a playlist of length j-t_i using the first i-1 songs such that the last two songs are not of the same genre
            else:
                dp2[i][j] = dp2[i-1][j] + dp2[i-1][j-songs[i-1][0]]

    # print(dp2)

    # dp3[i][j] = number of ways to make a playlist of length j using the first i songs such that the last two songs are not of the same genre and the last song is not the same as the first song
    dp3 = [[0 for j in range(T+1)] for i in range(n+1)]
    dp3[0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            # if we can't use the ith song, then the number of ways to make a playlist of length j such that the last two songs are not of the same genre and the last song is not the same as the first song is the same as the number of ways to make a playlist of length j using the first i-1 songs such that the last two songs are not of the same genre and the last song is not the same as the first song
            if j < songs[i-1][0]:
                dp3[i][j] = dp3[i-1][j]
            # if we can use the ith song, then the number of ways to make a playlist of length j such that the last two songs are not of the same genre and the last song is not the same as the first song is the sum of the number of ways to make a playlist of length j using the first i-1