
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(tuple(map(int, sys.stdin.readline().split())))
    songs.sort()
    songs = tuple(songs)
    print(solve(songs, T))

def solve(songs, T):
    """
    >>> solve(((1, 1), (1, 2), (1, 3)), 3)
    6
    >>> solve(((1, 1), (1, 1), (1, 3)), 3)
    2
    >>> solve(((5, 3), (2, 1), (3, 2), (5, 1)), 10)
    10
    """
    MOD = 10**9 + 7
    cache = {}
    def count_playlists(songs, T):
        if (songs, T) in cache:
            return cache[(songs, T)]
        if T == 0:
            return 1
        if not songs:
            return 0
        if T < 0:
            return 0
        result = 0
        for i in range(len(songs)):
            if i > 0 and songs[i][1] == songs[i-1][1]:
                continue
            result += count_playlists(songs[:i] + songs[i+1:], T - songs[i][0])
            result %= MOD
        cache[(songs, T)] = result
        return result
    return count_playlists(songs, T)

if True:
    main()