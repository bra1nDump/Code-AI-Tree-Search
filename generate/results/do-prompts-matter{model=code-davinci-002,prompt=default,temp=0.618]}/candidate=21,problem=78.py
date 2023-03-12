

def solve(n, T, t_g_list):
    dp = [[[0 for _ in range(3)] for _ in range(T + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    # t_g_list.sort(key=lambda x: x[0])
    for i in range(1, n + 1):
        for j in range(T + 1):
            if j < t_g_list[i - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                for k in range(3):
                    if k == t_g_list[i - 1][1] - 1:
                        continue
                    dp[i][j][k] += dp[i - 1][j][k]
                    dp[i][j][t_g_list[i - 1][1] - 1] += dp[i - 1][j - t_g_list[i - 1][0]][k]

    return sum(dp[-1][-1]) % 1000000007


def main():
    n, T = [int(x) for x in input().split()]
    t_g_list = []
    for _ in range(n):
        t, g = [int(x) for x in input().split()]
        t_g_list.append((t, g))
    print(solve(n, T, t_g_list))


if True:
    main()