
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain time with a certain genre.
# The first dimension will be the time and the second dimension will be the genre.
# We will use the following formula to calculate the number of ways to reach a certain time with a certain genre:
# dp[time][genre] = dp[time - song_time][genre] + dp[time - song_time][genre - 1] + dp[time - song_time][genre + 1]
# This formula is based on the idea that we can reach a certain time with a certain genre by reaching a time that is
# song_time less with the same genre or with the genre before or after.
# We will use a modulo to avoid overflow.

# Time complexity: O(n * T)
# Space complexity: O(T)

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    dp[0][0] = 1
    for time in range(1, T + 1):
        for genre in range(1, 4):
            for song in songs:
                if time - song[0] >= 0:
                    dp[time][genre] += dp[time - song[0]][genre]
                    if genre > 1:
                        dp[time][genre] += dp[time - song[0]][genre - 1]
                    if genre < 3:
                        dp[time][genre] += dp[time - song[0]][genre + 1]
                    dp[time][genre] %= 1000000007
    return dp[T][0]

n, T = map(int, input().split())
songs = []
for _ in range(n):
    songs.append(list(map(int, input().split())))
print(solve(n, T, songs))