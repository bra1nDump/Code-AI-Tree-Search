
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain time with a certain genre.
# The first dimension will be the time and the second dimension will be the genre.
# We will use the following formula to calculate the number of ways to reach a certain time with a certain genre:
# dp[time][genre] = dp[time - song_time][genre] + dp[time - song_time][genre - 1] + dp[time - song_time][genre + 1]
# The first term in the sum is the number of ways to reach the time with the genre if we don't play the song.
# The second term is the number of ways to reach the time with the genre if we play the song and the genre of the song is genre - 1.
# The third term is the number of ways to reach the time with the genre if we play the song and the genre of the song is genre + 1.
# We will use the following base cases:
# dp[0][0] = 1
# dp[time][0] = 0 if time > 0
# dp[0][genre] = 0 if genre > 0
# We will use the following formula to calculate the answer:
# answer = dp[T][1] + dp[T][2] + dp[T][3]
# The answer is the sum of the number of ways to reach the time T with each genre.

# Time complexity: O(n * T)
# Space complexity: O(T)

MOD = 10**9 + 7

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    dp[0][0] = 1
    for time in range(1, T + 1):
        for genre in range(1, 4):
            dp[time][genre] = dp[time][genre - 1]
            if time >= songs[genre][0]:
                dp[time][genre] += dp[time - songs[genre][0]][genre]
                if genre > 1:
                    dp[time][genre] += dp[time - songs[genre][0]][genre - 1]
                if genre < 3:
                    dp[time][genre] += dp[time - songs[genre][0]][genre + 1]
            dp[time][genre] %= MOD
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    songs = [[0, 0] for _ in range(4)]
    for _ in range(n):
        song_time, song_genre = map(int, input().split())
        songs[song_genre][0] = song_time
        songs[song_genre][1] += 1
    print(solve(n, T, songs))