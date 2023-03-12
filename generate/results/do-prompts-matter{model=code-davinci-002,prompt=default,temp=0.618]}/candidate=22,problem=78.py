
import itertools

def main():
    # read parameters
    n, t = (int(x) for x in input().split())
    songs = [(int(x), int(y)) for x, y in input().split()]
    # create a list of all possible combinations
    combinations = [x for x in itertools.combinations(songs, n)]
    # count combinations
    count = 0
    for combination in combinations:
        count += 1 if sum(x[0] for x in combination) == t else 0

    print(count)

if True:
    main()