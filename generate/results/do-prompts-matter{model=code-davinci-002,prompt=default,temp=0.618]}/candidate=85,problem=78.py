
#-------------------------------------------------------------------------------

def input_list():
    """
    Reads a line of input as a list of integers.
    
    :return: the list of integers
    """
    return [int(x) for x in input().split()]

def solve(n, T, songs):
    """
    Solves the problem.
    
    :param n: the number of songs
    :param T: the total duration
    :param songs: a 2D array of the songs, where each row is a song (first
                  element is the duration, second element is the genre)
    :return: the number of different playlist sequences
    """
    # The idea is to use dynamic programming.
    # Let f[i][j] be the number of different playlist sequences of length i
    # ending in a song of genre j.
    # Then f[i][j] = f[i - 1][1] + f[i - 1][2] + f[i - 1][3] - f[i - 1][j]
    # if the last song is not the same genre as the song before it, and
    # f[i][j] = f[i - 1][j] otherwise.
    # The array f is not needed, but it is useful for understanding the
    # solution.
    # The solution is f[T][1] + f[T][2] + f[T][3]
    # The base case is f[0][j] = 1 for all j.
    f = [[0 for j in range(4)] for i in range(T + 1)]
    for j in range(4):
        f[0][j] = 1
    for i in range(1, T + 1):
        for j in range(1, 4):
            if songs[i - 1][1] != j:
                f[i][j] = (f[i - 1][1] + f[i - 1][2] + f[i - 1][3]
                           - f[i - 1][j])
            else:
                f[i][j] = f[i - 1][j]
    return (f[T][1] + f[T][2] + f[T][3]) % (10**9 + 7)

#-------------------------------------------------------------------------------

def main():
    n, T = input_list()
    songs = [input_list() for i in range(n)]
    print(solve(n, T, songs))

if True:
    main()