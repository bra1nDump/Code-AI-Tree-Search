
def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))

    # dp[i][j][k] = number of ways to get to the i-th song with a total duration of j minutes ending with the k-th genre
    # dp[i][j][k] = sum(dp[i-1][j-t][l]) for all l != k
    dp = [[[0]*4 for _ in range(T+1)] for _ in range(n+1)]
    dp[0][0][0] = 1

    for i in range(1, n+1):
        for j in range(T+1):
            for k in range(4):
                if j < songs[i-1][0]:
                    continue
                for l in range(1, 4):
                    if l == k:
                        continue
                    dp[i][j][k] += dp[i-1][j-songs[i-1][0]][l]

    ans = 0
    for j in range(T+1):
        for k in range(4):
            ans += dp[n][j][k]

    return ans

print(main())