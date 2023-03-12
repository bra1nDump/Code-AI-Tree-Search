
def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))
    songs.sort()
    dp = [[0 for _ in range(T + 1)] for _ in range(n)]
    for i in range(n):
        for t in range(T + 1):
            if i == 0:
                if t == songs[i][0]:
                    dp[i][t] = 1
            else:
                if t >= songs[i][0]:
                    dp[i][t] = dp[i - 1][t] + dp[i - 1][t - songs[i][0]]
                else:
                    dp[i][t] = dp[i - 1][t]
    print(dp[n - 1][T])

if True:
    main()