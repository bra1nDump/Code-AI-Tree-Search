
import sys

def count_playlists(num_songs, total_duration):
    count = 0

    return count

def main():
    # read input
    num_songs, total_duration = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(num_songs):
        duration, genre = map(int, sys.stdin.readline().split())
        songs.append((duration, genre))

    # compute and print answer
    count = count_playlists(num_songs, total_duration)
    print(count)

if True:
    main()