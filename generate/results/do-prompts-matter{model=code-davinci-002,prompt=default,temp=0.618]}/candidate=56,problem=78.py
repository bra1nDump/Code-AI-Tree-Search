

def f(n, t, songs, dp):
    if n == 0 and t == 0:
        return 1
    if n == 0 or t == 0:
        return 0
    if dp[n][t]:
        return dp[n][t]

    def solve(t, genre):
        if t == 0:
            return 1
        if t < 0:
            return 0
        return sum([f(n - 1, t - songs[i][0], songs[:i] + songs[i + 1:], dp)
                    for i in range(len(songs)) if songs[i][1] != genre])

    dp[n][t] = solve(t, 0) - solve(t, 1) - solve(t, 2) - solve(t, 3)
    return dp[n][t]


def main():
    n, t = (int(x) for x in input().split())
    songs = [[int(x) for x in input().split()] for _ in range(n)]
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    print(f(n, t, songs, dp) % (10 ** 9 + 7))


if True:
    main()