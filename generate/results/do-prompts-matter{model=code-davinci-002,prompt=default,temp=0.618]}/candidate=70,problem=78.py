
# Solution 1: DFS with memoization
#
# This problem can be solved by a DFS search with memoization.
#
# The key observation is that, if we are at the $i$-th song and we have $k$ minutes left, then there are only $3$ possible genres
# we can choose from.
#
# The function dfs(i, k) counts the number of playlists that can be made by choosing the $i$-th song and having $k$ minutes left.
#
# The time complexity is O(n * T * 3) = O(225 * 15 * 3) = O(15000).

MOD = 10**9 + 7

def dfs(i, k):
    if (i, k) in dp:
        return dp[(i, k)]
    elif i == n:
        return int(k == 0)
    else:
        ans = 0
        for g in range(1, 4):
            if g == genres[i] and k >= durations[i]:
                ans += dfs(i + 1, k - durations[i])
            elif g != genres[i] and k >= durations[i] - 1:
                ans += dfs(i + 1, k - durations[i] + 1)
        dp[(i, k)] = ans
        return ans

n, T = map(int, input().split())
durations = []
genres = []
for i in range(n):
    t, g = map(int, input().split())
    durations.append(t)
    genres.append(g)
dp = {}
print(dfs(0, T))


# Solution 2: Dynamic programming
#
# The function dp(i, k) counts the number of playlists that can be made by choosing the $i$-th song and having $k$ minutes left.
#
# The time complexity is O(n * T * 3) = O(225 * 15 * 3) = O(15000).
#
# The space complexity is O(n * T * 3) = O(225 * 15 * 3) = O(15000).

MOD = 10**9 + 7

def dp(n, T):
    c = [[[0] * 4 for _ in range(T + 1)] for _ in range(n + 1)]
    c[0][0][0] = 1
    for i in range(1, n + 1):
        for k in range(T + 1):
            for g in range(1, 4):
                if g == genres[i - 1]:
                    if k >= durations[i - 1]:
                        c[i][k][g] = c[i - 1][k - durations[i - 1]][0]
                else:
                    if k >= durations[i - 1] - 1:
                        c[i][k][g] = c[i - 1][k - durations[i - 1] + 1][0]
    ans = 0
    for i in range(1, n + 1):
        for k in range(T + 1):
            ans += c[i][k][0]
    return ans

n, T = map(int, input().split())
durations = []
genres = []
for i in range(n):
    t, g = map(int, input().split())
    durations.append(t)
    genres.append(g)
print(dp(n, T))