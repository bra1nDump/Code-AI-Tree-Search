
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j][k] = number of ways to make a playlist of length i with last song of genre j and last song of length k
    dp = [[[0 for _ in range(16)] for _ in range(4)] for _ in range(T+1)]
    dp[0][0][0] = 1
    for i in range(1, T+1):
        for j in range(1, 4):
            for k in range(1, 16):
                for song in songs:
                    if song[0] == k and song[1] == j:
                        for l in range(1, 4):
                            for m in range(1, 16):
                                if i - k >= 0:
                                    dp[i][j][k] += dp[i-k][l][m]
    ans = 0
    for j in range(1, 4):
        for k in range(1, 16):
            ans += dp[T][j][k]
    return ans % (10**9 + 7)

if True:
    main()