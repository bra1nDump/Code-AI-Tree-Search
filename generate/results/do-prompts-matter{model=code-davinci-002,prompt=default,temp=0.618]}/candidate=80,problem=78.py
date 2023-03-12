

def get_all_playlists(n, T):
    """
    @param n: number of songs
    @param T: total duration
    @return: number of different sequences of songs, the total duration is exactly T, such that there are no two
             consecutive songs of the same genre in them and all the songs in the playlists are different
    """
    mod = int(1e9 + 7)

    # duration and genre for each song
    durations = [0] * n
    genres = [0] * n

    # the number of ways to make a playlist of the length i with the last song of genre j
    # i is the length of the playlist, j is the genre of the last song
    dp = [[0] * 4 for _ in range(T + 1)]

    # load data
    for i in range(n):
        durations[i], genres[i] = map(int, input().split())

    # initialization
    # base case: T = 1
    # the number of ways to make a playlist of length 1 with the last song of genre j is the number of songs of genre j
    for j in range(1, genres[-1] + 1):
        dp[1][j] = genres.count(j)

    # dp[i][j] = the number of ways to make a playlist of length i with the last song of genre j
    for i in range(2, T + 1):
        for j in range(1, genres[-1] + 1):
            # the number of ways to make a playlist of length i with the last song of genre j is the sum of the number
            # of ways to make a playlist of length i - t with the last song of genre k, where 1 <= k <= 3, k != j, and t
            # is the duration of the last song of genre j
            dp[i][j] = sum(dp[i - durations[-1]][k] for k in range(1, genres[-1] + 1) if k != j)

    # # print dp table
    # for row in dp:
    #     print(row)

    return sum(dp[T]) % mod


def main():
    # read the number of test cases
    t = int(input())

    for _ in range(t):
        # read the number of songs and total duration
        n, T = map(int, input().split())

        # print the number of different sequences of songs, the total duration is exactly T, such that there are no two
        # consecutive songs of the same genre in them and all the songs in the playlist are different
        print(get_all_playlists(n, T))


if True:
    main()