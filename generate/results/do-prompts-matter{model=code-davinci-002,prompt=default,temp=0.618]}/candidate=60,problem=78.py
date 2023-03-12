
from sys import stdin, stdout
from collections import defaultdict
from fractions import gcd

# def input():
#     return stdin.readline().strip()

# def print(s):
#     stdout.write(str(s))

def solve():
    n, T = map(int, input().split())
    genres = defaultdict(list)
    for i in range(n):
        t, g = map(int, input().split())
        genres[g].append(t)

    dp = [0 for _ in range(T + 1)]
    dp[0] = 1

    for g in genres.values():
        for t in g:
            for i in range(T, t - 1, -1):
                # dp[i] += dp[i - t]
                dp[i] = (dp[i] + dp[i - t]) % 1000000007

    # print(dp)
    return dp[T]

print(solve())