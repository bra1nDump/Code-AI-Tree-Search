
import sys
sys.setrecursionlimit(10000) # Default limit is 1000

import re
import math
import itertools

def get_input(file):
    lines = [line.rstrip('\n') for line in open(file)]
    n_t = re.split(r'\s+', lines[0].rstrip('\n'))
    n = int(n_t[0])
    t = int(n_t[1])
    songs = []
    for i in range(1, n+1):
        song = re.split(r'\s+', lines[i].rstrip('\n'))
        songs.append({'t':int(song[0]), 'g':int(song[1])})
    return n, t, songs

def get_combinations_count(t, songs):
    songs_by_length = {}
    for song in songs:
        if song['t'] in songs_by_length:
            songs_by_length[song['t']].append(song)
        else:
            songs_by_length[song['t']] = [song]
    songs_by_length_keys = sorted(songs_by_length.keys(), reverse=True)

    count = 0
    for i in range(1, len(songs_by_length_keys)+1):
        for songs_set in itertools.combinations(songs_by_length_keys, i):
            total_seconds = sum(songs_set)
            if total_seconds == t:
                songs_pool = []
                for song_length in songs_set:
                    songs_pool += songs_by_length[song_length]
                songs_pool_combinations = itertools.permutations(songs_pool)
                songs_pool_combinations_filtered = []
                for songs_pool_combination in songs_pool_combinations:
                    if check_combination(songs_pool_combination):
                        songs_pool_combinations_filtered.append(songs_pool_combination)
                count += len(songs_pool_combinations_filtered)
    return count % (10**9 + 7)

def check_combination(songs):
    for i in range(1, len(songs)):
        if songs[i]['g'] == songs[i-1]['g']:
            return False
    return True


def main():
    n, t, songs = get_input('input.txt')
    print(get_combinations_count(t, songs))


if True:
    main()