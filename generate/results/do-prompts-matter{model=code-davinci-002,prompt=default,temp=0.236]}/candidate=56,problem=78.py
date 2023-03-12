
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, sys.stdin.readline().split())))
    # print(songs)
    # print(n, T)

    # dp[i][j] = number of ways to make a playlist of length i with last song genre j
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    dp[0][0] = 1
    for i in range(1, T + 1):
        for j in range(1, 4):
            for song in songs:
                if song[0] == i and song[1] == j:
                    dp[i][j] += sum(dp[i - song[0]][k] for k in range(1, 4) if k != j)
                    dp[i][j] %= 1000000007
    # print(dp)
    print(sum(dp[T][j] for j in range(1, 4)))

if True:
    main()