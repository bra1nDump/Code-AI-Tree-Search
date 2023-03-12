
class Songs:
    def __init__(self, total, songs):
        self.T = total
        self.songs = songs
        self.songs.sort(key=lambda s: s[0])
        self.n = len(self.songs)
        self.sums = [0]
        for song in self.songs:
            self.sums.append(self.sums[-1] + song[0])

    def numPlaylists(self):
        # The DP table. The value of dp[i][j] will be the number of playlists
        # of length i that ends with a song in genre j.
        dp = [[0] * 4 for _ in range(self.T + 1)]
        dp[0][0] = 1
        for i in range(1, self.T + 1):
            for j in range(1, 4):
                # The number of songs with duration i and genre j.
                count = sum(1 for song in self.songs if song == (i, j))
                # If there is no song with duration i and genre j, we cannot
                # make a playlist of length i that ends with a song in genre j.
                if not count:
                    continue
                # If there is no song with duration i - 1, we can only make a
                # playlist of length i that ends with a song in genre j if there
                # is only one song with duration i and genre j.
                if i - 1 == 0:
                    if count == 1:
                        dp[i][j] = 1
                # Otherwise, we can make a playlist of length i that ends with a
                # song in genre j if we pair it with any playlist of length i - 1
                # that does not end with a song in genre j.
                else:
                    dp[i][j] = count * dp[i - 1][j - 1]
                # We can also make such a playlist if we pair the song with any
                # playlist of length i - t where t is the duration of the song and
                # we do not consider the last song.
                for k in range(1, i - self.sums[count] + 1):
                    dp[i][j] += dp[i - k][j]
                # Subtract the number of invalid playlists.
                for k in range(1, count):
                    dp[i][j] -= dp[i - k][j - 1]
        return sum(dp[self.T]) % (10 ** 9 + 7)

if True:
    n, T = map(int, input().split())
    songs = [tuple(map(int, input().split())) for _ in range(n)]
    print(Songs(T, songs).numPlaylists())