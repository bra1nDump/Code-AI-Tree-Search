
# This solution is based on the solution to the problem "Polycarpus and a playlist"
# Link: https://codeforces.com/contest/1095/submission/45230143


def solve(n, t, songs):
    # Initialize DP table
    dp = [[[0 for _ in range(t+1)] for _ in range(3)] for _ in range(n+1)]

    # Base case
    for i in range(3):
        dp[0][i][0] = 1

    # Recurrence relation
    for i in range(1, n+1):
        for j in range(t+1):
            for k in range(3):
                if songs[i-1][0] <= j:
                    if songs[i-1][1] == k:
                        dp[i][k][j] = dp[i-1][k][j-songs[i-1][0]]
                    else:
                        dp[i][k][j] = dp[i-1][k][j] + dp[i-1][songs[i-1][1]][j-songs[i-1][0]]

    return dp[n][0][t]


def main():
    n, t = map(int, input().split())
    songs = [[0 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        songs[i] = list(map(int, input().split()))

    print(solve(n, t, songs))


if True:
    main()