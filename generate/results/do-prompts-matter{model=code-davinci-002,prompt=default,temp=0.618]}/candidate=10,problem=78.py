
import sys
import math

# def get_input():
#     n, T = map(int, sys.stdin.readline().split())
#     song_list = []
#     for i in range(n):
#         t_i, g_i = map(int, sys.stdin.readline().split())
#         song_list.append((t_i, g_i))
#     return n, T, song_list

def get_input(file):
    with open(file, 'r') as f:
        n, T = map(int, f.readline().split())
        song_list = []
        for i in range(n):
            t_i, g_i = map(int, f.readline().split())
            song_list.append((t_i, g_i))
        return n, T, song_list

def main():
    # n, T, song_list = get_input()
    n, T, song_list = get_input('rosalind_ba10b.txt')
    # print(n, T, song_list)
    modulo = 10**9 + 7
    final_count = 0
    # print(song_list)
    # print(song_list[0])
    genre = {}
    for i in range(1, 4):
        genre[i] = []
    for i in range(n):
        # print(song_list[i][1])
        genre[song_list[i][1]].append(song_list[i][0])
    # print(genre)

    for i in range(1, 4):
        # print(i, genre[i])
        temp_count = 0
        for j in range(len(genre[i])):
            # print(genre[i][j])
            temp_count += int(T/genre[i][j])
        # print(temp_count)
        if temp_count > 0:
            final_count += int(math.factorial(temp_count) / (math.factorial(temp_count - len(genre[i])) * math.factorial(len(genre[i]))))
    # print(final_count)
    print(final_count % modulo)

if True:
    main()