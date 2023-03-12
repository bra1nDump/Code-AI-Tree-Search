
import sys
# import math
# import collections
# import itertools

# def do_something(x):
#     return x

# def main():
#     sys.setrecursionlimit(100000)
#     reader = (int(x) for x in sys.stdin.read().split())
#     n, T = next(reader), next(reader)
#     a = [next(reader) for i in range(n)]
#     print(do_something(x))
#     return 0

# if True:
#     main()

def t(n, T, dp):
    if n < 1 or T < 0:
        return 0
    if T == 0:
        return 1

    if dp[n][T] is not None:
        return dp[n][T]

    dp[n][T] = 0
    for i in range(1, 4):
        dp[n][T] += t(n-1, T-i, dp)
    dp[n][T] = dp[n][T] % 1000000007

    return dp[n][T]

def main():
    sys.setrecursionlimit(100000)
    reader = (int(x) for x in sys.stdin.read().split())
    n, T = next(reader), next(reader)
    a = [next(reader) for i in range(n)]
    dp = [[None for i in range(T+1)] for j in range(n+1)]
    print(t(n, T, dp))
    return 0

if True:
    main()