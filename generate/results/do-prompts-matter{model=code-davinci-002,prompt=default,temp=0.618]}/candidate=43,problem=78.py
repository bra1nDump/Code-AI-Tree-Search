


def count_playlists(n, T, t, g):
	dp = [[[0 for k in range(4)] for j in range(T + 1)] for i in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, T + 1):
			for k in range(1, 4):
				if t[i - 1] <= j:
					if g[i - 1] != k:
						dp[i][j][k] += dp[i - 1][j - t[i - 1]][k] + dp[i - 1][j - t[i - 1]][k - 1]
					else:
						dp[i][j][k] += dp[i - 1][j - t[i - 1]][k - 1]
				else:
					dp[i][j][k] = dp[i - 1][j][k]

	ans = 0
	for k in range(1, 4):
		ans += dp[n][T][k]
	return ans


def main():
	n, T = [int(x) for x in input().split()]
	t = [0]
	g = [0]
	for i in range(n):
		ti, gi = [int(x) for x in input().split()]
		t.append(ti)
		g.append(gi)
	print(count_playlists(n, T, t, g))


if True:
	main()