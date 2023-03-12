from sys import stdin
from collections import defaultdict

def main():
    n, t = map(int, stdin.readline().split())
    songs = defaultdict(lambda: 0)
    for i in range(n):
        song_time, song_genre = map(int, stdin.readline().split())
        songs[(song_time, song_genre)] += 1

    if t < 2 or n < 2 or t > (3 * n):
        return 0

    # dp_table[genre][time] = number of ways
    dp_table = [[0] * (t + 1) for i in range(4)]
    dp_table[0][0] = 1
    dp_table[1][0] = 1
    dp_table[2][0] = 1
    dp_table[3][0] = 1

    for song_time, song_genre in songs.keys():
        for time in range(t + 1):
            if time - song_time >= 0:
                # can add song
                dp_table[song_genre][time] += dp_table[song_genre - 1][time - song_time]
                for genre in range(1, 4):
                    if genre != song_genre:
                        dp_table[song_genre][time] += dp_table[genre][time - song_time]

    return dp_table[3][t] % (10 ** 9 + 7)

print(main())