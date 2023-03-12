
# Solution 1
#
# def solve(n, T, songs):
#     """
#     n: number of songs
#     T: total duration
#     songs: list of tuples (duration, genre)
#     """
#     # dp[i][j] = number of playlists of length i with total duration j
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#     dp[0][0] = 1
#     for i in range(1, n + 1):
#         for j in range(T + 1):
#             for k in range(j + 1):
#                 if songs[i - 1][0] == k:
#                     dp[i][j] += dp[i - 1][j - k]
#     return dp[n][T]
#
#
# def main():
#     n, T = map(int, input().split())
#     songs = []
#     for _ in range(n):
#         songs.append(tuple(map(int, input().split())))
#     print(solve(n, T, songs))
#
#
# if True:
#     main()

# Solution 2
#
# def solve(n, T, songs):
#     """
#     n: number of songs
#     T: total duration
#     songs: list of tuples (duration, genre)
#     """
#     # dp[i][j] = number of playlists of length i with total duration j
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#     dp[0][0] = 1
#     for i in range(1, n + 1):
#         for j in range(T + 1):
#             for k in range(j + 1):
#                 if songs[i - 1][0] == k:
#                     dp[i][j] += dp[i - 1][j - k]
#     return dp[n][T]
#
#
# def main():
#     n, T = map(int, input().split())
#     songs = []
#     for _ in range(n):
#         songs.append(tuple(map(int, input().split())))
#     print(solve(n, T, songs))
#
#
# if True:
#     main()

# Solution 3
#
# def solve(n, T, songs):
#     """
#     n: number of songs
#     T: total duration
#     songs: list of tuples (duration, genre)
#     """
#     # dp[i][j] = number of playlists of length i with total duration j
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#     dp[0][0] = 1
#     for i in range(1, n + 1):
#         for j in range(T + 1):
#             for k in range(j + 1):
#                 if songs[i - 1][0] == k:
#                     dp[i][j] += dp[i - 1][j - k]
#     return dp[n][T]
#
#
# def main():
#     n, T = map(int, input().split())
#     songs = []
#     for _ in range(n):
#         songs.append(tuple(map(int, input().split())))
#     print(solve(n, T, songs))
#
#
# if True:
#     main()

# Solution 4
#
# def solve(n, T, songs):
#     """
#     n: number of songs
#     T: total duration
#     songs: list of tuples (duration, genre)
#     """
#     # dp[i][j] = number of playlists of length i with total duration j
#     dp = [[0 for _ in range(T + 1)] for _ in range(n + 1)]
#     dp[0][0] = 1
#     for i in range(1, n + 1):
#         for j in