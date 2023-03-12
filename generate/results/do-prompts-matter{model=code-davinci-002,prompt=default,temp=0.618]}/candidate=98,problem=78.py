

def solve(n, T, songs):
    """
    Dynamic programming solution.
    The idea is to use a 3D array to store the number of possible playlists ending with
    a song of a certain duration and genre.
    The first dimension corresponds to the ending duration of the playlist, the second
    dimension corresponds to the genre of the last song and the third dimension
    corresponds to the second last song.
    """

    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(T + 1)]

    # Base cases:
    # 1. The playlist is empty
    for g in range(4):
        dp[0][g][0] = 1
    # 2. The playlist has a single song
    for s in songs:
        dp[s[0]][s[1]][0] += 1

    # Iterate through all possibilities
    for g in range(1, 4):
        for s in songs:
            for t in range(T + 1):
                # We can only take songs that are shorter than the remaining duration
                if s[0] <= t:
                    # The playlist's ending duration is the current duration minus the duration of the current song
                    dp[t][s[1]][g] += dp[t - s[0]][s[1]][g - 1]

    # The answer is the sum of all possible ending durations, ending genres and second last genres
    return sum(sum(sum(dp[t][g][h] for h in range(4)) for g in range(4)) for t in range(T + 1)) % (10 ** 9 + 7)


def main():
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    print(solve(n, T, songs))


if True:
    main()