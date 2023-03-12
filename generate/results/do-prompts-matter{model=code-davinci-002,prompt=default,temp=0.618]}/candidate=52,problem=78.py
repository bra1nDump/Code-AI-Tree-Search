
import sys
import os
import time
from collections import defaultdict
from functools import lru_cache

class Problem(object):
    def __init__(self, s):
        self.s = s # input string
        self.n, self.T = self._parse()
        self.songs = self._parse_songs()
        #print(self.n, self.T, self.songs)

    def _parse(self):
        self.s = self.s.split('\n')
        n, T = [int(x) for x in self.s[0].split()]
        return n, T

    def _parse_songs(self):
        songs = []
        for i in range(1, self.n+1):
            t, g = [int(x) for x in self.s[i].split()]
            songs.append([t, g])
        return songs

    def solve(self):
        #print('solving')
        ans = self._solve()
        return ans

    def _solve(self):
        #print('solving')
        @lru_cache(maxsize=None)
        def helper(i, T, last_genre):
            #print(i, T, last_genre)
            if i == 0:
                if T == 0:
                    return 1
                else:
                    return 0
            ans = 0
            t, g = self.songs[i-1]
            if T >= t and g != last_genre:
                ans += helper(i-1, T-t, g)
            ans += helper(i-1, T, last_genre)
            return ans

        ans = helper(self.n, self.T, -1)
        return ans


def main():
    #sys.stdin = open('test.in', 'r')
    #sys.stdout = open('test.out', 'w')
    problem = Problem(sys.stdin.read())
    ans = problem.solve()
    print(ans)

if True:
    main()