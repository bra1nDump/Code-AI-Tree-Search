
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain time with a certain genre.
# The first dimension will be the time and the second dimension will be the genre.
# We will use the following formula to calculate the number of ways to reach a certain time with a certain genre:
# dp[time][genre] = dp[time - song_time][genre] + dp[time - song_time][genre - 1] + dp[time - song_time][genre + 1]
# The first term is the number of ways to reach the current time with the current genre by using the current song.
# The second term is the number of ways to reach the current time with the current genre by using the current song and a song of the previous genre.
# The third term is the number of ways to reach the current time with the current genre by using the current song and a song of the next genre.
# We will use the following base cases:
# dp[0][1] = 1
# dp[0][2] = 1
# dp[0][3] = 1
# The answer will be the sum of the number of ways to reach the total time with each genre.

# Time complexity: O(n * T)
# Space complexity: O(T)

MOD = 10**9 + 7

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    dp[0][1] = 1
    dp[0][2] = 1
    dp[0][3] = 1
    for song_time, song_genre in songs:
        for time in range(T, song_time - 1, -1):
            dp[time][song_genre] = (dp[time][song_genre] + dp[time - song_time][song_genre]) % MOD
            if song_genre > 1:
                dp[time][song_genre] = (dp[time][song_genre] + dp[time - song_time][song_genre - 1]) % MOD
            if song_genre < 3:
                dp[time][song_genre] = (dp[time][song_genre] + dp[time - song_time][song_genre + 1]) % MOD
    return sum(dp[T]) % MOD

if True:
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        song_time, song_genre = map(int, input().split())
        songs.append((song_time, song_genre))
    print(solve(n, T, songs))