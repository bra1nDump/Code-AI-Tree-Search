
def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort()
    # print(songs)
    dp = [[[0 for _ in range(T+1)] for _ in range(4)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(T+1):
                if dp[i][j][k] == 0:
                    continue
                for l in range(i+1, n):
                    if songs[l][1] == j:
                        continue
                    if k + songs[l][0] > T:
                        break
                    dp[l+1][songs[l][1]][k+songs[l][0]] += dp[i][j][k]
                    dp[l+1][songs[l][1]][k+songs[l][0]] %= 10**9 + 7
    # print(dp)
    ans = 0
    for i in range(n+1):
        for j in range(T+1):
            ans += dp[i][3][j]
            ans %= 10**9 + 7
    print(ans)

if True:
    main()