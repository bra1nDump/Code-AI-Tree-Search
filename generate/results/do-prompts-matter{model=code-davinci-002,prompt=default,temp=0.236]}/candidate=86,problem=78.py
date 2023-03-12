
# Solution 1
#
# def solve(n, T, songs):
#     # dp[i][j] = number of ways to make a playlist of length j using the first i songs
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#
#     # base case: dp[0][0] = 1
#     dp[0][0] = 1
#
#     for i in range(1, n + 1):
#         for j in range(1, T + 1):
#             # if the song is too long, we can't use it
#             if j < songs[i - 1][0]:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 # we can either use the song or not use it
#                 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
#
#     return dp[n][T]
#
#
# n, T = map(int, input().split())
# songs = []
# for _ in range(n):
#     songs.append(tuple(map(int, input().split())))
#
# print(solve(n, T, songs))

# Solution 2
#
# def solve(n, T, songs):
#     # dp[i][j] = number of ways to make a playlist of length j using the first i songs
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#
#     # base case: dp[0][0] = 1
#     dp[0][0] = 1
#
#     for i in range(1, n + 1):
#         for j in range(1, T + 1):
#             # if the song is too long, we can't use it
#             if j < songs[i - 1][0]:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 # we can either use the song or not use it
#                 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
#
#     return dp[n][T]
#
#
# n, T = map(int, input().split())
# songs = []
# for _ in range(n):
#     songs.append(tuple(map(int, input().split())))
#
# print(solve(n, T, songs))

# Solution 3
#
# def solve(n, T, songs):
#     # dp[i][j] = number of ways to make a playlist of length j using the first i songs
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#
#     # base case: dp[0][0] = 1
#     dp[0][0] = 1
#
#     for i in range(1, n + 1):
#         for j in range(1, T + 1):
#             # if the song is too long, we can't use it
#             if j < songs[i - 1][0]:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 # we can either use the song or not use it
#                 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i - 1][0]]
#
#     return dp[n][T]
#
#
# n, T = map(int, input().split())
# songs = []
# for _ in range(n):
#     songs.append(tuple(map(int, input().split())))
#
# print(solve(n, T, songs))

# Solution 4
#
# def solve(n, T, songs):
#     # dp[i][j] = number of ways to make a playlist of length j using the first i songs
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#