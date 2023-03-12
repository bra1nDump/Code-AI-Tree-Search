
import sys
import math
sys.setrecursionlimit(100000)

class Solution:
    def __init__(self):
        self.d = {}
        self.m = 10 ** 9 + 7

    def solve(self, nums, t):
        if t < 0:
            return 0
        if t == 0:
            return 1
        if (t, nums) in self.d:
            return self.d[(t, nums)]
        ans = 0
        for i in range(len(nums)):
            ans += self.solve(nums[:i] + nums[i + 1:], t - nums[i][0])
            ans %= self.m
        self.d[(t, nums)] = ans
        return ans

if True:
    n, t = [int(x) for x in input().split()]
    nums = []
    for i in range(n):
        t1, g = [int(x) for x in input().split()]
        nums.append((t1, g))
    s = Solution()
    print(s.solve(nums, t))