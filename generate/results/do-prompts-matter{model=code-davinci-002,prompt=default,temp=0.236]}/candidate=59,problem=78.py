
from sys import stdin
from collections import defaultdict

MOD = 10**9 + 7

def main():
    n, T = map(int, stdin.readline().split())
    songs = []
    for _ in range(n):
        t, g = map(int, stdin.readline().split())
        songs.append((t, g))
    songs.sort()
    dp = defaultdict(int)
    dp[0] = 1
    for t, g in songs:
        for k, v in dp.items():
            if k + t <= T:
                dp[k + t] += v
                if g in dp:
                    dp[k + t] -= dp[g]
    print(dp[T] % MOD)

if True:
    main()