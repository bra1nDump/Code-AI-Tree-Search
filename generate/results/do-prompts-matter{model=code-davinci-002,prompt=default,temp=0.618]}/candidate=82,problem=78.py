
import itertools

# Main
n, t = [int(i) for i in input().split()]
songs = []
for i in range(n):
    songs.append([int(i) for i in input().split()])

# Get permutations of songs that sum up to t.
permutations = []
for i in range(1, n+1):
    for perm in itertools.combinations(songs, i):
        if sum([x[0] for x in perm]) == t:
            permutations.append(perm)

# Get permutations of songs that sum up to t and don't have consecutive genres.
valid_permutations = []
for perm in permutations:
    valid = True
    for i in range(len(perm)-1):
        if perm[i][1] == perm[i+1][1]:
            valid = False
    if valid:
        valid_permutations.append(perm)

print(len(valid_permutations) % (10**9 + 7))