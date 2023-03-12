
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    MOD = 10 ** 9 + 7
    # dp[i][j] = number of ways to make a playlist of length i with last song of genre j
    dp = [[0 for j in range(4)] for i in range(T + 1)]
    dp[0][0] = 1
    for i in range(1, T + 1):
        for j in range(4):
            for song in songs:
                if song[0] <= i and song[1] != j:
                    dp[i][song[1]] += dp[i - song[0]][j]
                    dp[i][song[1]] %= MOD
    return sum(dp[T]) % MOD

if True:
    main()