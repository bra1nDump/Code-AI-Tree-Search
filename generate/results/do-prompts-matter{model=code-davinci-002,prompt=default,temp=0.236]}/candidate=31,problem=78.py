
# Solution

def solution(n, T, songs):
    # dp[i][j] = number of ways to make a playlist of length i with last song of genre j
    dp = [[0] * 4 for _ in range(T + 1)]
    dp[0][0] = 1
    for i in range(1, T + 1):
        for j in range(1, 4):
            for song in songs:
                if song[0] <= i and song[1] == j:
                    dp[i][j] += dp[i - song[0]][j - 1]
    return sum(dp[T]) % (10 ** 9 + 7)

n, T = map(int, input().split())
songs = []
for _ in range(n):
    songs.append(list(map(int, input().split())))
print(solution(n, T, songs))