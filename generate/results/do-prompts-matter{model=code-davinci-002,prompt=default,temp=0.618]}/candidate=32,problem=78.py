
from collections import defaultdict
from itertools import combinations

T, n = map(int, input().split())

songs = []
genre_map = defaultdict(list)

for i in range(n):
    t, g = map(int, input().split())
    songs.append((t, g))
    genre_map[g].append(t)

def get_all_combos(t, g):
    combos = []
    for i in range(1, t//min(genre_map[g]) + 1):
        combos.extend(combinations(genre_map[g], i))
    combos.append([t])
    return combos

def get_all_subsets(t, g):
    subsets = []
    for i in range(1, t//min(genre_map[g]) + 1):
        subsets.extend(combinations(genre_map[g], i))
    return subsets

def reduce_subset(subset):
    while len(subset) > 1:
        if subset[0] == subset[1]:
            subset.pop(0)
        else:
            break
    return subset

def get_combos(t, g):
    combos = []
    subsets = get_all_subsets(t, g)
    for i in range(len(subsets)):
        if sum(subsets[i]) == t:
            combos.append(subsets[i])
        elif sum(subsets[i]) < t:
            subset = reduce_subset(subsets[i])
            if sum(subset) + min(genre_map[g]) <= t:
                combos.extend(get_combos(t - sum(subset), g))
    return combos

def remove_duplicates(combos):
    for i in range(len(combos)):
        for j in range(len(combos[i])):
            combos[i][j] = tuple(combos[i][j])
    combos = set(combos)
    combos = [list(x) for x in combos]
    return combos

def get_all_combos(t, g):
    combos = get_combos(t, g)
    combos = remove_duplicates(combos)
    return combos

def get_combos(t, g):
    combos = []
    subsets = get_all_subsets(t, g)
    for i in range(len(subsets)):
        if sum(subsets[i]) == t:
            combos.append(subsets[i])
        elif sum(subsets[i]) < t:
            subset = reduce_subset(subsets[i])
            if sum(subset) + min(genre_map[g]) <= t:
                combos.extend(get_combos(t - sum(subset), g))
    return combos

def remove_duplicates(combos):
    for i in range(len(combos)):
        for j in range(len(combos[i])):
            combos[i][j] = tuple(combos[i][j])
    combos = set(combos)
    combos = [list(x) for x in combos]
    return combos

def get_all_combos(t, g):
    combos = get_combos(t, g)
    combos = remove_duplicates(combos)
    return combos

def get_combos(t, g):
    combos = []
    subsets = get_all_subsets(t, g)
    for i in range(len(subsets)):
        if sum(subsets[i]) == t:
            combos.append(subsets[i])
        elif sum(subsets[i]) < t:
            subset = reduce_subset(subsets[i])
            if sum(subset) + min(genre_map[g]) <= t:
                combos.extend(get_combos(t - sum(subset), g))
    return combos

def remove_duplicates(combos):
    for i in range(len(combos)):
        for j in range(len(combos[i])):
            combos[i][j] = tuple(combos[i][j])