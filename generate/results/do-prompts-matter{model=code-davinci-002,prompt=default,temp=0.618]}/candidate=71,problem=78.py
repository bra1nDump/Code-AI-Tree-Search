
import sys

def solve(n, t, l):
    from collections import defaultdict
    from functools import lru_cache

    d = defaultdict(dict)

    for i, (dur, gen) in enumerate(l):
        d[dur][gen] = i

    @lru_cache(maxsize=None)
    def dfs(i, last_dur, last_gen, curr_t):
        if curr_t == t:
            return 1

        if curr_t > t:
            return 0

        ans = 0

        for dur in d:
            if dur > t - curr_t:
                continue

            if dur == last_dur:
                continue

            for gen in d[dur]:
                if gen == last_gen:
                    continue

                ans += dfs(d[dur][gen], dur, gen, curr_t + dur)

        return ans

    return dfs(-1, -1, -1, 0)

def main():
    n, t = list(map(int, sys.stdin.readline().split()))
    l = []
    for _ in range(n):
        dur, gen = list(map(int, sys.stdin.readline().split()))
        l.append((dur, gen))

    ans = solve(n, t, l)
    print(ans)

if True:
    main()