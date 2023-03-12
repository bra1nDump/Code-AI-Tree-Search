

def main():
    n, T = map(int, input().split())
    durations = list()
    genres = list()
    for _ in range(n):
        t, g = map(int, input().split())
        durations.append(t)
        genres.append(g)

    # dp[i][j] = number of ways to make playlist of duration i with last song of genre j
    dp = [ [0 for g in range(4)] for i in range(T+1)]
    dp[0][0] = 1

    for i in range(T+1):
        for j in range(1, 4):
            for k in range(n):
                if genres[k] != j and durations[k] <= i:
                    dp[i][j] += dp[i - durations[k]][genres[k]]

    print(sum(dp[T]) % (10**9 + 7))


if True:
    main()