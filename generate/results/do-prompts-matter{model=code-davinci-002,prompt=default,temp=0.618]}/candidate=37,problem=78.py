
import math
import sys

MAX_N = 15
MAX_G = 3
MAX_T = 225
MAX_P = 1000000007

state = [[[0 for t in range(MAX_T + 1)] for g in range(MAX_G + 1)] for n in range(MAX_N + 1)]


def solve(n, T, t, g):
    if state[n][g][T] == 0:
        if n == 0 or T == 0:
            state[n][g][T] = 1
        else:
            state[n][g][T] = solve(n - 1, T, t, g)
            if T >= t[n - 1]:
                state[n][g][T] += solve(n - 1, T - t[n - 1], t, g)
                if g[n - 1] != g:
                    state[n][g][T] += solve(n - 1, T - t[n - 1], t, g[n - 1])
        state[n][g][T] %= MAX_P
    return state[n][g][T]


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, T = next(reader)
    t = [0] + list(next(reader) for _ in range(n))
    g = [0] + list(next(reader) for _ in range(n))
    print(solve(n, T, t, g))


if True:
    main()