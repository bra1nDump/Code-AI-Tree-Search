
def calc_songs(song_num, total_time, songs, cache):
    if total_time == 0:
        return 1
    if song_num == 0:
        return 0
    if (song_num, total_time) in cache:
        return cache[(song_num, total_time)]
    if songs[song_num][0] > total_time:
        return calc_songs(song_num - 1, total_time, songs, cache)
    count = 0
    # Don't use this song
    count += calc_songs(song_num - 1, total_time, songs, cache)
    # Use this song
    count += calc_songs(song_num - 1, total_time - songs[song_num][0], songs, cache)
    cache[(song_num, total_time)] = count
    return count

def main():
    n, t = map(int, input().split())
    songs = [0]
    for i in range(n):
        d, g = map(int, input().split())
        songs.append((d, g))
    cache = {}
    print(calc_songs(n, t, songs, cache))

if True:
    main()