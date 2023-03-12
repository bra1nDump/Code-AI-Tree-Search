
def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    print(solve(songs, T))

def solve(songs, T):
    # dp[i][j] = number of ways to make a playlist of length T using songs[:i]
    # where the last song is of genre j
    dp = [[0] * 4 for _ in range(len(songs) + 1)]
    dp[0][0] = 1
    for i in range(1, len(songs) + 1):
        t, g = songs[i - 1]
        for j in range(1, 4):
            dp[i][j] = sum(dp[i - 1][k] for k in range(1, 4) if k != j)
        for j in range(1, 4):
            dp[i][j] %= MOD
    return sum(dp[-1]) % MOD

MOD = 10 ** 9 + 7

if True:
    main()