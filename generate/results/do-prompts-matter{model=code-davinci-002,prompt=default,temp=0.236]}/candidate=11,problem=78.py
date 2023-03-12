
def main():
    n, T = map(int, input().split())
    songs = []
    for i in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j][k] = number of ways to make a playlist of length i with last song of genre j and last song of length k
    dp = [[[0 for k in range(T + 1)] for j in range(4)] for i in range(T + 1)]
    dp[0][0][0] = 1
    for i in range(1, T + 1):
        for j in range(4):
            for k in range(T + 1):
                if dp[i - 1][j][k] > 0:
                    for song in songs:
                        if song[0] <= i and song[1] != j:
                            dp[i][song[1]][song[0]] += dp[i - 1][j][k]
    return sum(dp[T][j][k] for j in range(4) for k in range(T + 1)) % (10 ** 9 + 7)

if True:
    main()