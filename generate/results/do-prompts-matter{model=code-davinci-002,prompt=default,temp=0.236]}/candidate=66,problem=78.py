

def main():
    n, T = map(int, input().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort()
    # print(songs)

    # dp[i][j] = number of ways to get to time j with song i
    dp = [[0 for _ in range(T+1)] for _ in range(n)]
    dp[0][songs[0][0]] = 1
    for i in range(1, n):
        for j in range(T+1):
            if j >= songs[i][0]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i][0]]
            else:
                dp[i][j] = dp[i-1][j]
            if songs[i][1] == songs[i-1][1]:
                dp[i][j] -= dp[i-2][j-songs[i][0]]
    # print(dp)
    print(dp[n-1][T])


if True:
    main()