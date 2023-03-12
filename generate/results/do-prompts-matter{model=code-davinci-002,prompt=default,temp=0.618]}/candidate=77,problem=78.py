
n, T = map(int, input().split())

songs = []
for _ in range(n):
    t, g = map(int, input().split())
    songs.append((t, g))

# dp[i][j] stores the number of different sequences of songs, the total length of exactly j, such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different.
dp = [[0] * (T + 1) for _ in range(n + 1)]

# Initialize the base cases.
for i in range(1, n + 1):
    for j in range(1, T + 1):
        if songs[i-1][0] > j:
            dp[i][j] = 0
        elif i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-songs[i-1][0]]) % (10**9 + 7)

print(dp[n][T])