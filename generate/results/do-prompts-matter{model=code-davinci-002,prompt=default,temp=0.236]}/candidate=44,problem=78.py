
import sys
import math

def main():
    # read input
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])

    # compute answer
    answer = 0
    for i in range(1 << n):
        # check if the total duration is correct
        total_duration = 0
        for j in range(n):
            if (i >> j) & 1:
                total_duration += songs[j][0]
        if total_duration != T:
            continue

        # check if there are two consecutive songs of the same genre
        genres = [0] * 4
        for j in range(n):
            if (i >> j) & 1:
                genres[songs[j][1]] += 1
        if max(genres) > 1:
            continue

        # if the playlist is valid, add it to the answer
        answer += 1

    # print answer
    print(answer)

if True:
    main()