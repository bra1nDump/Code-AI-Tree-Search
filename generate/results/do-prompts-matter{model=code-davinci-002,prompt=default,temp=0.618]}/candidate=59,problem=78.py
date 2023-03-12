
import sys

def get_answer(n, t, durations, genres):
    dp = [[[0 for x in range(t + 1)] for y in range(n + 1)] for z in range(4)]
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            dp[genres[i]][i][j] = dp[genres[i]][i - 1][j]
            if j - durations[i] >= 0:
                dp[genres[i]][i][j] += dp[genres[i]][i - 1][j - durations[i]]
            if genres[i] != genres[i - 1]:
                dp[genres[i]][i][j] += dp[genres[i - 1]][i - 1][j - durations[i]]
    return dp[3][n][t]


# n, t = map(int, sys.stdin.readline().split())
# durations = [0]
# genres = [0]
# for i in range(n):
#     line = list(map(int, sys.stdin.readline().split()))
#     durations.append(line[0])
#     genres.append(line[1])
# print(get_answer(n, t, durations, genres))

"""
Tests
"""

def test_get_answer():
    assert get_answer(3, 3, [0, 1, 1, 1], [0, 1, 2, 3]) == 6
    assert get_answer(3, 3, [0, 1, 1, 1], [0, 1, 1, 3]) == 2
    assert get_answer(4, 10, [0, 5, 2, 3, 5], [0, 3, 1, 2, 1]) == 10