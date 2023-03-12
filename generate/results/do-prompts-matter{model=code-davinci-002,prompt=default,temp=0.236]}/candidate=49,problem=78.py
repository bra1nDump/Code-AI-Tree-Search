
def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort()
    # print(songs)

    # dp[i][j][k] = number of ways to make a playlist of length j with the last song being song i and the last song's genre being k
    dp = [[[0 for _ in range(4)] for _ in range(T+1)] for _ in range(n)]

    # base case: first song
    dp[0][songs[0][0]][songs[0][1]] = 1

    for i in range(1, n):
        for j in range(1, T+1):
            for k in range(1, 4):
                if j >= songs[i][0]:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-songs[i][0]][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k]

                if k == songs[i][1]:
                    dp[i][j][k] -= dp[i-1][j-songs[i][0]][k]

    # print(dp)
    ans = 0
    for i in range(1, 4):
        ans += dp[n-1][T][i]
    print(ans % 1000000007)

if True:
    main()