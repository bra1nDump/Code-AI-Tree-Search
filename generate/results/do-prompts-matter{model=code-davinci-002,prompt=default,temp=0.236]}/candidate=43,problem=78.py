
def main():
    n, T = map(int, input().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort()
    # print(songs)
    dp = [[0 for _ in range(T+1)] for _ in range(n)]
    for i in range(n):
        if songs[i][0] <= T:
            dp[i][songs[i][0]] = 1
    for i in range(n):
        for j in range(T+1):
            if dp[i][j] > 0:
                for k in range(i+1, n):
                    if songs[k][0] + j <= T and songs[k][1] != songs[i][1]:
                        dp[k][j+songs[k][0]] += dp[i][j]
    # print(dp)
    ans = 0
    for i in range(n):
        ans += dp[i][T]
    print(ans)

if True:
    main()