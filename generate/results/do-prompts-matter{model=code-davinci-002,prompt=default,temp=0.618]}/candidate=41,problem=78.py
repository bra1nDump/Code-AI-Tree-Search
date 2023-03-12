
import sys
import math

# f_rec(n, m, k, d) - number of valid sequences of length n, 
# with m songs, last song of type k, and total duration d
f_rec = {}

def f(n, m, k, d):
    if n == 0:
        if d == 0:
            return 1
        else:
            return 0
    elif f_rec.get((n, m, k, d)) != None:
        return f_rec.get((n, m, k, d))
    else:
        total = 0
        for i in range(1, m+1):
            if song_duration[i-1] <= d:
                if song_genres[i-1] == k:
                    total += f(n-1, m, k, d-song_duration[i-1])
                else:
                    total += f(n-1, m, song_genres[i-1], d-song_duration[i-1])
        f_rec[(n, m, k, d)] = total
        return total

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    num_songs, total_duration = next(reader)
    global song_duration, song_genres
    song_duration = []
    song_genres = []
    for _ in range(num_songs):
        duration, genre = next(reader)
        song_duration.append(duration)
        song_genres.append(genre)
    print(f(num_songs, num_songs, 0, total_duration) % (10**9 + 7))

if True:
    main()