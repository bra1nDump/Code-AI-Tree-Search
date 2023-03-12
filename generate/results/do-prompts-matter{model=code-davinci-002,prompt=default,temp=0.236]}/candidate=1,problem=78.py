
import sys
import math

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    # print(songs)

    # dp[i][j] = number of ways to make a playlist of length j using the first i songs
    dp = [[0 for j in range(T+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= songs[i-1][0]:
                dp[i][j] += dp[i-1][j-songs[i-1][0]]
    # print(dp)

    # dp2[i][j] = number of ways to make a playlist of length j using the first i songs,
    # such that the last song is of genre j
    dp2 = [[0 for j in range(T+1)] for i in range(n+1)]
    dp2[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            dp2[i][j] = dp2[i-1][j]
            if j >= songs[i-1][0] and songs[i-1][1] == j:
                dp2[i][j] += dp2[i-1][j-songs[i-1][0]]
    # print(dp2)

    # dp3[i][j] = number of ways to make a playlist of length j using the first i songs,
    # such that the last song is of genre j and the second to last song is of genre k
    dp3 = [[[0 for j in range(T+1)] for k in range(4)] for i in range(n+1)]
    dp3[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            for k in range(4):
                dp3[i][j][k] = dp3[i-1][j][k]
                if j >= songs[i-1][0] and songs[i-1][1] == j and k == j:
                    dp3[i][j][k] += dp3[i-1][j-songs[i-1][0]][k]
                elif j >= songs[i-1][0] and songs[i-1][1] == j and k != j:
                    dp3[i][j][k] += dp3[i-1][j-songs[i-1][0]][k]
    # print(dp3)

    # dp4[i][j] = number of ways to make a playlist of length j using the first i songs,
    # such that the last song is of genre j and the second to last song is of genre k
    # and the third to last song is of genre l
    dp4 = [[[[0 for j in range(T+1)] for k in range(4)] for l in range(4)] for i in range(n+1)]
    dp4[0][0][0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            for k in range(4):
                for l in range(4):
                    dp4[i][j][k][l] = dp4[i-1][j][k][l]
                    if j >= songs[i-1][0] and songs[i-1][1] == j and k == j and l == j:
                        dp4[i][j][k][l] += dp4[i-1][j-songs[i-1][0]][k][l]
                    elif j >= songs[i-1][0] and songs[i-1][1] == j and k != j and l == j:
                        dp4[i][j][k][l] += dp4