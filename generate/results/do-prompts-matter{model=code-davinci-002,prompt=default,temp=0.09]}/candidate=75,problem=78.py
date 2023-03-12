
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of ways to reach a certain duration with a certain genre.
# The first dimension will be the duration and the second dimension will be the genre.
# We will use the following formula to calculate the number of ways to reach a certain duration with a certain genre:
# dp[duration][genre] = dp[duration - song_duration][genre] + dp[duration - song_duration][genre - 1] + dp[duration - song_duration][genre + 1]
# The first term in the above formula is the number of ways to reach the current duration with the current genre by using the current song.
# The second term is the number of ways to reach the current duration with the current genre by using the current song and the previous song.
# The third term is the number of ways to reach the current duration with the current genre by using the current song and the next song.
# We will use the above formula to calculate the number of ways to reach a certain duration with a certain genre.
# We will use the following formula to calculate the answer:
# answer = dp[duration][1] + dp[duration][2] + dp[duration][3]
# The first term in the above formula is the number of ways to reach the current duration with the first genre.
# The second term is the number of ways to reach the current duration with the second genre.
# The third term is the number of ways to reach the current duration with the third genre.
# We will use the above formula to calculate the answer.

# Time complexity: O(n * T)
# Space complexity: O(T)

MOD = 10 ** 9 + 7

def solve(n, T, songs):
    dp = [[0 for _ in range(4)] for _ in range(T + 1)]
    dp[0][1] = 1
    dp[0][2] = 1
    dp[0][3] = 1
    for duration in range(1, T + 1):
        for genre in range(1, 4):
            for song in songs:
                if duration - song[0] >= 0:
                    dp[duration][genre] += dp[duration - song[0]][genre]
                    if genre - 1 >= 1:
                        dp[duration][genre] += dp[duration - song[0]][genre - 1]
                    if genre + 1 <= 3:
                        dp[duration][genre] += dp[duration - song[0]][genre + 1]
                    dp[duration][genre] %= MOD
    answer = 0
    for genre in range(1, 4):
        answer += dp[T][genre]
        answer %= MOD
    return answer

if True:
    n, T = map(int, input().split())
    songs = []
    for _ in range(n):
        t, g = map(int, input().split())
        songs.append((t, g))
    print(solve(n, T, songs))