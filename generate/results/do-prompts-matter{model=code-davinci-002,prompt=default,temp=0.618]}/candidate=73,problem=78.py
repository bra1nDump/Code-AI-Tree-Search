

def count_playlists(T, songs):
    """
    This function is based on the idea of dynamic programming.

    Let $dp(i, j)$ be the number of playlists consisting of $i$ songs with the total duration of $j$ minutes.
    Then $dp(i, j) = \sum_{k=1}^n dp(i-1, j-t_k)$ if $t_k \le j$, where $n$ is the total number of songs,
    and $dp(i, j) = 0$ otherwise.

    $dp(i, j)$ can be precomputed in the table of size $n \times T$ in $O(n \cdot T)$.

    Thus, the answer is $dp(n, T)$.

    :param T: integer, the required total duration
    :param songs: list of lists, each sublist contains the duration of the song and its genre
    :return: integer, the number of different sequences of songs, the total length of exactly $T$,
    such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different
    """

    # the constant modulo
    mod = 10 ** 9 + 7

    # the number of songs
    n = len(songs)

    # the table dp[i][j] is assigned the number of playlists consisting of i songs with the total duration of j minutes
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # the first row is filled with zeros
    # the first column is filled with zeros except dp[0][0], which is assigned 1
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            dp[i][j] = 0
            for k in range(i):
                if songs[k][0] <= j:
                    dp[i][j] += dp[i - 1][j - songs[k][0]]
                    dp[i][j] %= mod

    return dp[n][T]


if True:
    # read the number of songs and the required total duration
    n, T = map(int, input().split())

    # read the duration of the song and its genre for each song
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append([t, g])

    # print the answer
    print(count_playlists(T, songs))