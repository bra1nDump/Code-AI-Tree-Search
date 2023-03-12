
import sys
import math

def main():
    n, t = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    # songs.sort(key=lambda x: x[1])
    print(songs)
    dp = [0] * (t + 1)
    dp[0] = 1
    for i in range(1, t + 1):
        for song in songs:
            if i - song[0] >= 0:
                print(song)
                dp[i] = (dp[i] + dp[i - song[0]]) % (int(1e9) + 7)
            print(dp)
    print(dp)
    print(dp[t])

# def main():
#     n, t = map(int, sys.stdin.readline().split())
#     songs = []
#     for i in range(n):
#         songs.append(list(map(int, sys.stdin.readline().split())))
#     # songs.sort(key=lambda x: x[1])
#     dp = [0] * (t + 1)
#     dp[0] = 1
#     for i in range(1, t + 1):
#         for song in songs:
#             if i - song[0] >= 0:
#                 dp[i] = (dp[i] + dp[i - song[0]]) % (int(1e9) + 7)
#     print(dp[t])

if True:
    main()