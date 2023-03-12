
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    # print(songs)
    # print(n, T)
    # print(songs)
    # print(songs[0][0])
    # print(songs[1][0])
    # print(songs[2][0])
    # print(songs[3][0])
    # print(songs[0][1])
    # print(songs[1][1])
    # print(songs[2][1])
    # print(songs[3][1])

    # dp[i][j] = number of ways to make a playlist of length j with songs 0..i
    # dp[i][j] = sum(dp[i-1][j-k]) for k in range(songs[i][0], T+1) if songs[i][1] != songs[i-1][1]
    dp = [[0 for j in range(T+1)] for i in range(n)]
    # print(dp)

    # base case
    for i in range(songs[0][0], T+1):
        dp[0][i] = 1
    # print(dp)

    # recursive case
    for i in range(1, n):
        for j in range(1, T+1):
            for k in range(songs[i][0], T+1):
                if songs[i][1] != songs[i-1][1]:
                    dp[i][j] += dp[i-1][j-k]
    # print(dp)

    print(dp[n-1][T])

if True:
    main()