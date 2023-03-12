
import functools
import functools

# Helper functions
def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoizer

def read_int():
    return int(input())

def read_int_map():
    return map(int, input().split(' '))

def read_int_list():
    return list(map(int, input().split(' ')))

def read_str():
    return input()

def read_char_list():
    return list(read_str())

def write_case_ans(i, ans):
    if isinstance(ans, list):
        ans = ' '.join([str(a) for a in ans])
    print('Case #%d: %s' % (i, ans))

def read_int_matrix():
    return [list(map(int, input().split(' '))) for _ in range(N)]

######################################################

def get_genres_dict(n, t, g):
    genres_dict = {}
    for i in range(n):
        if g[i] not in genres_dict:
            genres_dict[g[i]] = []
        genres_dict[g[i]].append((t[i], i))
    return genres_dict

@memoize
def get_num_playlists(n, t, g, t_rem, genres_dict):
    if t_rem == 0:
        # Base case
        return 1
    if n == 0:
        # Base case
        return 0
    num_playlists = 0
    for genre, song_list in genres_dict.items():
        for song_t, song_i in song_list:
            if song_t > t_rem:
                # song is too long for remaining time
                continue
            # try to add this song
            genres_dict_copy = genres_dict.copy()
            genres_dict_copy[genre].remove((song_t, song_i))
            if len(genres_dict_copy[genre]) == 0:
                del genres_dict_copy[genre]
            num_playlists += get_num_playlists(n-1, t, g, t_rem-song_t, genres_dict_copy)
    return num_playlists

if True:
    n, t = read_int_map()
    t = list(t)
    g = list(read_int_map())
    genres_dict = get_genres_dict(n, t, g)
    ans = get_num_playlists(n, t, g, t, genres_dict)
    print(ans)