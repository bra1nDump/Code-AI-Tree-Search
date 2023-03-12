
import sys

def main():
    """
    Main function.
    """

    # Get input
    line = sys.stdin.readline().strip().split()
    songs = []
    for _ in range(int(line[0])):
        songs.append([int(value) for value in sys.stdin.readline().strip().split()])

    # Calculate
    result = 0
    cache = {}
    for i in range(len(songs)):
        for j in range(len(songs)):
            if i != j:
                result += calculate(songs, i, j, int(line[1]), cache)
    print(result)

def calculate(songs, i, j, time_left, cache):
    """
    Calculate the number of valid playlists.
    """

    # Validate
    if (i, j, time_left) in cache.keys():
        return cache[(i, j, time_left)]
    if time_left < 0:
        return 0

    # Base cases
    if time_left == 0:
        return 1
    if i == j and songs[i][0] == time_left:
        return 1
    if i == j and songs[i][0] != time_left:
        return 0

    # Recursive cases
    result = 0
    for k in range(len(songs)):
        if k != i and k != j and songs[k][1] != songs[j][1]:
            result += calculate(songs, j, k, time_left - songs[j][0], cache)
    cache[(i, j, time_left)] = result
    return result

if True:
    main()