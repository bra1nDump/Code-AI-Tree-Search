
T, N = map(int, input().split())
songs = []
for i in range(N):
  t, g = map(int, input().split())
  songs.append((t, g))
  
# dp[i][t][g] = number of playlists of length t using the first i songs that ended with the song of genre g
dp = [[[0 for i in range(4)] for j in range(T+1)] for k in range(N+1)]

def add(x, y):
  return (x + y) % 1000000007

for i in range(1, N+1):
  for t in range(1, T+1):
    for g in range(1, 4):
      if t >= songs[i-1][0] and songs[i-1][1] != g:
        dp[i][t][g] = add(dp[i][t][g], dp[i-1][t-songs[i-1][0]][songs[i-1][1]])
      for g2 in range(1, 4):
        if t >= songs[i-1][0] and g2 != g and g2 != songs[i-1][1]:
          dp[i][t][g] = add(dp[i][t][g], dp[i-1][t-songs[i-1][0]][g2])
      dp[i][t][g] = add(dp[i][t][g], dp[i-1][t][g])

result = 0
for i in range(1, N+1):
  for g in range(1, 4):
    result = add(result, dp[i][T][g])

print(result)