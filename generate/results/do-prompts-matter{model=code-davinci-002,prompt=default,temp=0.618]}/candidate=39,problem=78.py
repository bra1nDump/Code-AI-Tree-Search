
n, T = [int(x) for x in input().split()]
songs = {}

for i in range(1, n + 1):
    t, g = [int(x) for x in input().split()]
    songs[i] = (t, g)

cache = [[0] * (T + 1) for _ in range(n + 1)]

# cache[i][j] = number of different sequences of songs, the total duration is exactly j,
# such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different,
# using songs 1, ..., i

# base case
for i in range(1, n + 1):
    cache[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, T + 1):
        if j - songs[i][0] >= 0:
            cache[i][j] = cache[i - 1][j] # not using the current song
            for k in range(1, i):
                if songs[k][1] != songs[i][1]:
                    cache[i][j] += cache[k - 1][j - songs[i][0]]

print(cache[n][T] % (10 ** 9 + 7))