
########## FUNCTIONS ##########

########## MAIN CODE ##########

n, t = [int(x) for x in input().split()]
T = [t] + [0]*n
G = [0]*n
for i in range(n):
  t, g = [int(x) for x in input().split()]
  T[i+1] = t
  G[i] = g

D = [1] + [0]*t
for i in range(n):
  for j in range(T[i+1], t+1):
    D[j] = (D[j] + D[j-T[i+1]]) % 10**9 + 7
  for j in range(t, T[i+1]-1, -1):
    if G[i] == G[i-1]:
      D[j] = (D[j] - D[j-T[i+1]] + 10**9 + 7) % 10**9 + 7

print(D[t])