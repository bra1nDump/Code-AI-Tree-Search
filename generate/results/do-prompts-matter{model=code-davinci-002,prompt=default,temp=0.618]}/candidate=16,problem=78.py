

def main():
    n, T = map(int, input().strip().split())
    durations = []
    genres = []
    for i in range(n):
        t, g = map(int, input().strip().split())
        durations.append(t)
        genres.append(g)
    dp = [[[0] * 4 for i in range(T)] for j in range(n)]
    # dp[i][j] = number of playlists with length j ending with song i
    # dp[i][j][k] = number of playlists with length j ending with song i and last genre k
    # dp[i][j][0] = number of playlists with length j ending with song i and last genre 0 (unused)
    # dp[i][j][1] = number of playlists with length j ending with song i and last genre 1
    # dp[i][j][2] = number of playlists with length j ending with song i and last genre 2
    # dp[i][j][3] = number of playlists with length j ending with song i and last genre 3
    for i in range(n):
        for j in range(T):
            for k in range(4):
                dp[i][j][k] = 0
    for i in range(n):
        for j in range(durations[i], T+1):
            # playlist of length j that ends with song i
            # ending with genre x
            g = genres[i]
            x = g
            # playlist of length j-durations[i] that ends with song i-1 and last genre x
            dp[i][j][x] = (dp[i][j][x] + dp[i-1][j-durations[i]][x]) % (10**9 + 7)
            # playlist of length j-durations[i] that ends with song i-1 and last genre !x
            for y in range(1, 4):
                if y == x:
                    continue
                dp[i][j][x] = (dp[i][j][x] + dp[i-1][j-durations[i]][y]) % (10**9 + 7)
    ans = 0
    for i in range(1, 4):
        ans = (ans + dp[n-1][T][i]) % (10**9 + 7)
    print(ans)


main()