
from collections import defaultdict

n, T = map(int, input().split())

# T = 225
# n = 15

# t = [5, 2, 3, 5]
# g = [3, 1, 2, 1]

t = []
g = []

for x in range(n):
    tt, gg = map(int, input().split())
    t.append(tt)
    g.append(gg)

# print(t)
# print(g)

# create a dictionary of the form:
# {genre: [list of durations]}
genre_durations = defaultdict(list)
for i in range(n):
    genre_durations[g[i]].append(t[i])

# print(genre_durations)


# create a dictionary of the form:
# {genre: [list of durations]}
# where each list of durations is sorted in ascending order
for k, v in genre_durations.items():
    genre_durations[k] = sorted(v)

# print(genre_durations)

# create a dictionary of the form:
# {genre: [list of durations]}
# where each list of durations is sorted in descending order
for k, v in genre_durations.items():
    genre_durations[k] = sorted(v, reverse=True)

# print(genre_durations)


# create a dictionary of the form:
# {genre: [[list of durations], [list of durations]]}
# where the first list of durations is sorted in ascending order
# and the second list of durations is sorted in descending order
genre_durations_asc_desc = defaultdict(list)
for k, v in genre_durations.items():
    genre_durations_asc_desc[k] = sorted(v), sorted(v, reverse=True)

# print(genre_durations_asc_desc)


# create a dictionary of the form:
# {genre: [list of durations]}
# where each list of durations is sorted in ascending order
# and no element of the list is greater than T
genre_durations = defaultdict(list)
for i in range(n):
    if t[i] <= T:
        genre_durations[g[i]].append(t[i])

# print(genre_durations)


# create a dictionary of the form:
# {genre: [list of durations]}
# where each list of durations is sorted in descending order
# and no element of the list is greater than T
for k, v in genre_durations.items():
    genre_durations[k] = sorted(v, reverse=True)

# print(genre_durations)


# create a dictionary of the form:
# {genre: [[list of durations], [list of durations]]}
# where the first list of durations is sorted in ascending order
# and the second list of durations is sorted in descending order
# and no element of each list is greater than T
genre_durations_asc_desc = defaultdict(list)
for k, v in genre_durations.items():
    genre_durations_asc_desc[k] = sorted(v), sorted(v, reverse=True)

# print(genre_durations_asc_desc)


# create a dictionary of the form:
# {genre: [[list of durations], [list of durations]]}
# where the first list of durations is sorted in ascending order
# and the second list of durations is sorted in descending order
# and no element of each list is greater than T
# and the first list of durations is not empty
genre_durations_asc_desc = defaultdict(list)
for k, v in genre_durations.items():
    if len(v) > 0:
        genre_durations_asc_desc[k] = sorted(v), sorted(v, reverse=True)

# print(genre_durations_asc_desc)


# create a dictionary of the form:
# {genre: [[list of durations], [list of durations]]}
# where the first list of durations is sorted in ascending order
# and the second list of durations is sorted in descending order
# and no element of each list is greater than T
# and the first list of durations is not empty