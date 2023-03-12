
# dp[i][j] = number of playlists that start with song i and end with song j

def parse_input():
    n, T = [int(x) for x in input().split()]
    songs = []
    for i in range(n):
        t, g = [int(x) for x in input().split()]
        songs.append((t, g))
    return n, T, songs

def solve(n, T, songs):
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n):
        for j in range(i+1, n):
            for k in range(i, j):
                if songs[k][1] != songs[j][1]:
                    dp[i][j] += dp[i][k]
    return dp[0][n-1]

if True:
    n, T, songs = parse_input()
    print(solve(n, T, songs))