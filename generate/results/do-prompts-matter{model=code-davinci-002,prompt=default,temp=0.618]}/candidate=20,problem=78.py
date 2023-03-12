

import sys
import math

sys.setrecursionlimit(100000)

# def solve(n, t, songs, mem):
#     if (n, t) in mem:
#         return mem[(n, t)]
#     elif n == 0 and t == 0:
#         return 1
#     elif n == 0:
#         return 0
#     elif t == 0:
#         return 1
#     else:
#         s = 0
#         for i in range(1, n + 1):
#             if t >= songs[i][0]:
#                 s += solve(i - 1, t - songs[i][0], songs, mem)
#         mem[(n, t)] = s
#
#         return s

def solve(n, t, songs, mem):
    if (n, t) in mem:
        return mem[(n, t)]
    elif n == 0 and t == 0:
        return 1
    elif n == 0:
        return 0
    elif t == 0:
        return 1
    else:
        s = 0
        for i in range(1, n + 1):
            if t >= songs[i][0]:
                s += solve(i - 1, t - songs[i][0], songs, mem)
        mem[(n, t)] = s

        return s

def main():
    n, t = map(int, input().split())
    songs = {}
    for i in range(1, n + 1):
        s = tuple(map(int, input().split()))
        songs[i] = s
    mem = {}
    s = solve(n, t, songs, mem)
    print(s)

if True:
    main()