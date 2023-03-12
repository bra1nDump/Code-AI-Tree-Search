
import sys

#sys.stdin = open("input.txt", "r")

n, T = map(int, input().split())

songs = []
for i in range(n):
    t, g = map(int, input().split())
    songs.append((t, g))

#print(songs)

# dp[i][j] = number of playlists of length i with total duration j
dp = [[0 for i in range(T+1)] for j in range(n+1)]

# base case
for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, T+1):
        # if the song is too long, we can't use it
        if j < songs[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            # if the song is the same genre as the previous song, we can't use it
            if i > 1 and songs[i-1][1] == songs[i-2][1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i-1][0]]

print(dp[n][T])