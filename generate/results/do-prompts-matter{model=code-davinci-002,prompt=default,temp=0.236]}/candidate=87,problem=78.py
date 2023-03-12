
# Solution 1
# This solution is not fast enough for the hard version.
# The hard version requires a dynamic programming solution.
def solve(n, T, songs):
    # Return the number of playlists of length T that can be made from the songs.
    # songs is a list of tuples (length, genre)
    # n is the number of songs
    # T is the total length of the playlist
    if T == 0:
        return 1
    if n == 0:
        return 0
    if T < 0:
        return 0
    # Either include the first song or don't
    # If we include the first song, we can't include any songs of the same genre
    # as the first song.
    # If we don't include the first song, we can include any song.
    # We can't include the first song if its length is greater than T.
    if songs[0][0] <= T:
        return solve(n, T - songs[0][0], songs[1:]) + solve(n - 1, T, songs[1:])
    else:
        return solve(n - 1, T, songs[1:])

def main():
    n, T = [int(x) for x in input().split()]
    songs = []
    for _ in range(n):
        t, g = [int(x) for x in input().split()]
        songs.append((t, g))
    print(solve(n, T, songs))

if True:
    main()