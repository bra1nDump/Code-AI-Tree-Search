
import sys

def main():
    n, T = [int(x) for x in input().split()]
    songs = []
    for i in range(n):
        t, g = [int(x) for x in input().split()]
        songs.append((t, g))
    songs = sorted(songs, key=lambda x: x[0])

    dp = [0] * (T + 1)
    dp[0] = 1
    for i in range(T + 1):
        for t, g in songs:
            if t <= i:
                dp[i] += dp[i - t]

    # print(dp)

    print(dp[T])

if True:
    main()