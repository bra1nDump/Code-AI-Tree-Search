
def get_playlist_count(n, T, songs):
    # songs is a list of tuples (duration, genre)
    # n is number of songs
    # T is total duration
    # return number of playlists of n songs with duration T

    # dp[i][j][k] is the number of playlists of length i with duration j ending in genre k
    dp = [[[0 for i in range(4)] for j in range(T+1)] for k in range(n+1)]
    for i in range(4):
        dp[1][songs[0][0]][i] = 1
    for i in range(2, n+1):
        for j in range(1, T+1):
            for k in range(1, 4):
                if j >= songs[i-1][0]:
                    dp[i][j][k] = (dp[i-1][j-songs[i-1][0]][k] + dp[i-1][j][k-1] + dp[i-1][j-songs[i-1][0]][k-1]) % 1000000007
                else:
                    dp[i][j][k] = (dp[i-1][j][k-1]) % 1000000007
    return dp[n][T][3]

def main():
    n, T = [int(i) for i in input().split()]
    songs = []
    for i in range(n):
        t, g = [int(i) for i in input().split()]
        songs.append((t, g))
    print(get_playlist_count(n, T, songs))

if True:
    main()