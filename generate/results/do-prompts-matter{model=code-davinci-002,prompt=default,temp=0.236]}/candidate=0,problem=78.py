
# Solution

# This solution is based on the following observation:
# Let's say we have a playlist of length T.
# If we have a song of length t, we can add it to the playlist if T - t >= 0.
# If we have a song of length t and genre g, we can add it to the playlist if T - t >= 0 and the previous song is not of genre g.

# This solution is a dynamic programming solution.
# We have a 3D array, where the first dimension is the length of the playlist, the second dimension is the genre of the last song, and the third dimension is the number of songs in the playlist.
# The value of the array is the number of playlists of the given length, genre, and number of songs.
# We can calculate the value of the array by looking at the previous values.

# The time complexity is O(T * n * 3), where T is the total length of the playlist and n is the number of songs.
# The space complexity is O(T * 3).

# The following solution is based on the solution of the problem "Music playlist" from the Russian Olympiad in Informatics.

MOD = 10 ** 9 + 7

def solve(n, T, songs):
    dp = [[[0 for _ in range(n + 1)] for _ in range(4)] for _ in range(T + 1)]
    dp[0][0][0] = 1
    for t in range(T + 1):
        for g in range(4):
            for k in range(n + 1):
                for song in songs:
                    if t - song[0] >= 0 and g != song[1]:
                        dp[t][song[1]][k + 1] += dp[t - song[0]][g][k]
                        dp[t][song[1]][k + 1] %= MOD
    return sum(dp[T][g][n] for g in range(4)) % MOD

if True:
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    print(solve(n, T, songs))