
T, N = map(int, input().split())

t = [0] * N
g = [0] * N
for i in range(N):
  t[i], g[i] = map(int, input().split())

def f(s):
    if s >= N:
        return int(s == T)
    if memo[s] != -1:
        return memo[s]
    res = 0
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            res += f(s + t[i]) * int(g[i] != g[s])
            used[i] = 0
    memo[s] = res % 1000000007
    return memo[s]

memo = [-1] * N
used = [0] * N
print(f(0))