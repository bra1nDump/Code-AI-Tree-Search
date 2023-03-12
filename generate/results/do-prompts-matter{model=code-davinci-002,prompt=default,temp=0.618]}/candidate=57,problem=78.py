
# Solution 1: backtracking
# Time complexity: O(3^n)

# def createPlaylist(arr, T, n, a, b, c, d):
# 	if T == 0 and len(d) == n: # len(d) is the number of songs in the playlist
# 		a.append(d)
# 		return
# 	if T < 0 or len(d) == n:
# 		return
# 	if len(b) > 0:
# 		createPlaylist(arr, T, n, a, b[1:], c, d + [b[0]])
# 	if len(c) > 0:
# 		createPlaylist(arr, T, n, a, b, c[1:], d + [c[0]])

# for _ in range(int(input())):
# 	n, T = map(int, input().split())
# 	arr = []
# 	for i in range(n):
# 		t, g = map(int, input().split())
# 		arr.append([t, g])
# 	a = []
# 	createPlaylist(arr, T, n, a, arr, arr, [])
# 	print(len(set(tuple(l) for l in a)))

# Solution 2: dynamic programming
# Time complexity: O(nT)

for _ in range(int(input())):
	n, T = map(int, input().split())
	arr = []
	for i in range(n):
		t, g = map(int, input().split())
		arr.append([t, g])
	dp = [[[0 for _ in range(T + 1)] for _ in range(4)] for _ in range(n + 1)]
	for i in range(n + 1):
		dp[i][0][0] = 1
	for j in range(1, n + 1):
		for k in range(1, 4):
			for l in range(1, T + 1):
				if arr[j - 1][1] != k:
					dp[j][k][l] = dp[j - 1][k][l]
				if arr[j - 1][0] <= l:
					dp[j][k][l] += dp[j - 1][arr[j - 1][1]][l - arr[j - 1][0]]
	print(dp[n][3][T])