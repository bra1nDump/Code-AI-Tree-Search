
import itertools

def solve(T, songs):
    """
    T: int
    songs: list of (t, g) where t is duration and g is genre
    return: number of unique playlists
    """
    # TODO: implement this
    res = 0
    for song in itertools.permutations(songs):
        if (sum([song[i][0] for i in range(len(song))]) == T) and (len(set([song[i][1] for i in range(len(song))])) == len(song)):
            res += 1
    return res

def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    res = solve(T, songs)
    print(res)

if True:
    main()