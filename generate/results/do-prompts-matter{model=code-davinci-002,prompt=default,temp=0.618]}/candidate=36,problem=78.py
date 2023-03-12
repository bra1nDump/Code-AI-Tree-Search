
import sys

def read_line_of_integers():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def read_integer():
    return int(sys.stdin.readline().strip())

def read_integer_array():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def read_integer_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(read_integer_array())
    return matrix

#------------------------------------------------------------------------------#

MODULO = 1000000007

def main():
    """
    This is a simple combinatorics problem
    """
    n, T = read_line_of_integers()
    songs = read_integer_matrix(n)
    song_lengths, song_genres = zip(*songs)
    assert len(song_lengths) == len(song_genres) == n
    assert all(1 <= genre <= 3 for genre in song_genres)
    assert all(1 <= length <= 15 for length in song_lengths)
    assert 1 <= T <= 225

    total_ways = 1
    for length in range(1, T+1):
        counter = 0
        for song_index, song_length in enumerate(song_lengths):
            if song_length == length:
                counter += 1
        total_ways = (total_ways * (counter + 1)) % MODULO
    print(total_ways)

if True:
    main()