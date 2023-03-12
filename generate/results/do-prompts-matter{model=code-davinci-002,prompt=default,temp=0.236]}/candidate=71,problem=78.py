
import sys

def main():
    # read input
    n, T = [int(x) for x in sys.stdin.readline().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in sys.stdin.readline().split()])

    # create a list of songs that have the same genre
    same_genre = []
    for i in range(1, 4):
        same_genre.append([])
        for j in range(n):
            if songs[j][1] == i:
                same_genre[i-1].append(songs[j][0])

    # create a list of songs that have different genres
    diff_genre = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i:
                diff_genre.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T
    diff_genre_T = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T:
                diff_genre_T.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-1
    diff_genre_T_minus_1 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-1:
                diff_genre_T_minus_1.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-2
    diff_genre_T_minus_2 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-2:
                diff_genre_T_minus_2.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-3
    diff_genre_T_minus_3 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-3:
                diff_genre_T_minus_3.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-4
    diff_genre_T_minus_4 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-4:
                diff_genre_T_minus_4.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-5
    diff_genre_T_minus_5 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-5:
                diff_genre_T_minus_5.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-6
    diff_genre_T_minus_6 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-6:
                diff_genre_T_minus_6.append(songs[j][0])

    # create a list of songs that have different genres, but are less than or equal to T-7
    diff_genre_T_minus_7 = []
    for i in range(1, 4):
        for j in range(n):
            if songs[j][1] != i and songs[j][0] <= T-7:
                diff_genre_T_minus_7.append(songs[j][0])

    # create a list of songs that have different genres,