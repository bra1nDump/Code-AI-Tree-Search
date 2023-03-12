
from sys import stdin
from collections import defaultdict


def solve(n, T, songs):
    cache = {}

    def g(i, t):
        if (i, t) in cache:
            return cache[i, t]
        if t < 0:
            return 0
        if i == n:
            return 1 if t == 0 else 0
        result = 0
        for j in range(1, 4):
            if songs[i][j] > 0:
                result += g(i + 1, t - j)
        cache[i, t] = result
        return result

    return g(0, T)


def main():
    n, T = map(int, stdin.readline().split())
    songs = defaultdict(int)
    for i in range(n):
        t, g = map(int, stdin.readline().split())
        songs[t, g] += 1
    print(solve(n, T, songs))


if True:
    main()