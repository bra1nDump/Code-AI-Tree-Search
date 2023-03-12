
# Solution

def get_number_of_playlists(n, T, songs):
    """
    >>> get_number_of_playlists(3, 3, [(1, 1), (1, 2), (1, 3)])
    6
    >>> get_number_of_playlists(3, 3, [(1, 1), (1, 1), (1, 3)])
    2
    >>> get_number_of_playlists(4, 10, [(5, 3), (2, 1), (3, 2), (5, 1)])
    10
    """
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(T + 1)] for _ in range(n + 1)] for _ in range(4)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            for k in range(1, 4):
                if j - songs[i - 1][0] >= 0:
                    dp[k][i][j] = dp[k][i - 1][j] + dp[k - 1][i - 1][j - songs[i - 1][0]]
                else:
                    dp[k][i][j] = dp[k][i - 1][j]
    return dp[3][n][T] % MOD


if True:
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))
    print(get_number_of_playlists(n, T, songs))