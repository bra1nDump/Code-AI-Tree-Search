
# Solution

# This solution is not optimized for large input. Please see the solution for the hard version for a better solution.


def get_answer(n, t, genres, durations):
    if t == 0:
        return 1
    if n == 0:
        return 0
    if (n, t) in cache:
        return cache[(n, t)]
    total = 0
    if durations[n - 1] <= t:
        total += get_answer(n - 1, t - durations[n - 1], genres, durations)
    if genres[n - 1] != genres[n - 2] and genres[n - 1] != genres[n - 3]:
        total += get_answer(n - 1, t, genres, durations)
    cache[(n, t)] = total
    return total


cache = {}
n, t = map(int, input().split())
genres = [0] * (n + 2)
durations = [0] * n
for i in range(n):
    durations[i], genres[i + 2] = map(int, input().split())
print(get_answer(n, t, genres, durations) % (10 ** 9 + 7))