
import sys

import numpy as np

def main():
    """
    This code is based on the idea that every subproblem (i.e. the number of sequences
    of a certain length that end with a certain set of genres) can be expressed as a
    sum of previous subproblems. In particular, a subproblem that ends with genres
    $[i, j, k]$ can be expressed as a sum of subproblems that end with genres $[i, j]$,
    $[j, k]$, and $[i, k]$. 
    """
    lines = sys.stdin.readlines()
    n, T = [int(x) for x in lines[0].split()]
    songs = [tuple(int(x) for x in line.split()) for line in lines[1:]]
    memo = {}
    def count_sequences(length, genres):
        """
        This is a recursive function that counts the number of distinct playlists
        that have length `length` and end with the genres in `genres`.

        This function is memoized.
        """
        if length == 0:
            return 1
        if genres in memo:
            return memo[genres]
        num_sequences = 0
        for song in songs:
            if song[1] in genres or song[0] > length:
                continue
            updated_genres = list(genres)
            updated_genres.append(song[1])
            updated_genres.sort()
            updated_genres = tuple(updated_genres)
            num_sequences += count_sequences(length - song[0], updated_genres)
        memo[genres] = num_sequences
        return num_sequences
    return count_sequences(T, tuple([])) % (10**9 + 7)

if True:
    print(main())