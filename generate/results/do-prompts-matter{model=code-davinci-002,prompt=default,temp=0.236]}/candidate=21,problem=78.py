
# Solution 1
# This solution is too slow.
# It is a brute force solution.
# It will be TLE.

# import sys
# sys.setrecursionlimit(100000)

# def dfs(t, g, n, T, dp):
#     if t == T:
#         return 1
#     if t > T:
#         return 0
#     if dp[t][g] != -1:
#         return dp[t][g]
#     ans = 0
#     for i in range(1, n + 1):
#         if t + times[i] <= T:
#             ans += dfs(t + times[i], genres[i], n, T, dp)
#     dp[t][g] = ans
#     return ans

# n, T = map(int, input().split())
# times = [0]
# genres = [0]
# for i in range(n):
#     t, g = map(int, input().split())
#     times.append(t)
#     genres.append(g)
# dp = [[-1] * 4 for _ in range(T + 1)]
# print(dfs(0, 0, n, T, dp))


# Solution 2
# This solution is too slow.
# It is a brute force solution.
# It will be TLE.

# import sys
# sys.setrecursionlimit(100000)

# def dfs(t, g, n, T, dp):
#     if t == T:
#         return 1
#     if t > T:
#         return 0
#     if dp[t][g] != -1:
#         return dp[t][g]
#     ans = 0
#     for i in range(1, n + 1):
#         if t + times[i] <= T:
#             ans += dfs(t + times[i], genres[i], n, T, dp)
#     dp[t][g] = ans
#     return ans

# n, T = map(int, input().split())
# times = [0]
# genres = [0]
# for i in range(n):
#     t, g = map(int, input().split())
#     times.append(t)
#     genres.append(g)
# dp = [[-1] * 4 for _ in range(T + 1)]
# print(dfs(0, 0, n, T, dp))


# Solution 3
# This solution is too slow.
# It is a brute force solution.
# It will be TLE.

# import sys
# sys.setrecursionlimit(100000)

# def dfs(t, g, n, T, dp):
#     if t == T:
#         return 1
#     if t > T:
#         return 0
#     if dp[t][g] != -1:
#         return dp[t][g]
#     ans = 0
#     for i in range(1, n + 1):
#         if t + times[i] <= T:
#             ans += dfs(t + times[i], genres[i], n, T, dp)
#     dp[t][g] = ans
#     return ans

# n, T = map(int, input().split())
# times = [0]
# genres = [0]
# for i in range(n):
#     t, g = map(int, input().split())
#     times.append(t)
#     genres.append(g)
# dp = [[-1] * 4 for _ in range(T + 1)]
# print(dfs(0, 0, n, T, dp))


# Solution 4
# This solution is too slow.
# It is a brute force solution.
# It will be TLE.

# import sys
# sys.setrecursionlimit(100000)

# def dfs(t, g, n, T, dp):
#     if t == T:
#         return 1
#     if t > T:
#         return 0
#     if dp[t][g] != -1:
#         return dp[t][g]
#     ans