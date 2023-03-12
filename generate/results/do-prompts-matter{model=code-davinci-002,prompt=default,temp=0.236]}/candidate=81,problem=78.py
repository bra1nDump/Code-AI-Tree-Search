
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    # print(songs)
    # print(songs[0][0])
    # print(songs[0][1])
    # print(songs[1][0])
    # print(songs[1][1])
    # print(songs[2][0])
    # print(songs[2][1])

    # print(songs[0][0] + songs[1][0] + songs[2][0])

    # print(songs[0][1] + songs[1][1] + songs[2][1])

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T)
    # print(songs[0][1] + songs[1][1] + songs[2][1] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T)

    # print(songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0] + songs[2][0] == T and songs[0][1] + songs[1][1] + songs[2][1] == T and songs[0][0] + songs[1][0]