

def count_playlists(tracks):
    """
    Counts the number of playlists of length T, given a list of tracks.
    Tracks is a list of tuples of the form (length, genre).
    """
    n = len(tracks)
    T = sum([t[0] for t in tracks])
    if n == 0:
        return 0
    if n == 1:
        return 1
    # dp[i][j] = number of playlists with length j, ending in track i
    dp = [[0 for _ in range(T + 1)] for _ in range(n)]
    # Initialize base cases
    for i in range(n):
        dp[i][tracks[i][0]] = 1
    # Iterate
    for j in range(1, T + 1):
        for i in range(n):
            # The last track played must be track i
            if j - tracks[i][0] >= 0:
                # Playlists without track i
                dp[i][j] += sum(dp[i][j - tracks[i][0]])
                # Playlists with track i
                for k in range(n):
                    if k != i and tracks[k][1] != tracks[i][1] and j - tracks[i][0] - tracks[k][0] >= 0:
                        dp[i][j] += dp[k][j - tracks[i][0] - tracks[k][0]]
    return sum(dp[i][T] for i in range(n))


def main():
    n, T = map(int, input().split())
    tracks = []
    for _ in range(n):
        tracks.append(tuple(map(int, input().split())))
    print(count_playlists(tracks) % (10**9 + 7))


if True:
    main()