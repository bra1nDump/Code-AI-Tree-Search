
n, T = [int(x) for x in input().split()]
songs = []
for i in range(n):
    t, g = [int(x) for x in input().split()]
    songs.append((t, g))

# dp[i][j] = number of ways to play i songs with total len j
dp = [[0 for j in range(T+1)] for i in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    t, g = songs[i-1]
    for j in range(T+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        elif j >= t:
            if g == 1:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-t]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-t] - dp[i-2][j-t]
print(dp[n][T] % (10**9 + 7))