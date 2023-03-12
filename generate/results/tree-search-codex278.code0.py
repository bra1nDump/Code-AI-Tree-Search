

def solve(n, t, songs):
    dp = [[0 for _ in range(t + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(t + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                if j == songs[i][0]:
                    dp[i][j] = 1
            else:
                if j >= songs[i][0]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - songs[i][0]]
                else:
                    dp[i][j] = dp[i - 1][j]

    # print(dp)
    return dp[n - 1][t] % (10 ** 9 + 7)


def main():
    n, t = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(tuple(map(int, input().split())))
    print(solve(n, t, songs))


if True:
    main()