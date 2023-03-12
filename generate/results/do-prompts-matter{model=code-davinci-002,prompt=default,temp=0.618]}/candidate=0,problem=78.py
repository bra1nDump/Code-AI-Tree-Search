

import time

def create_playlist(n, t, g):
    if n == 1:
        if t[0] == T:
            return 1
        else:
            return 0
    else:
        res = 0
        for i in range(n):
            if i == 0:
                res += create_playlist(n-1, t[1:], g[1:])
            elif i == n-1:
                res += create_playlist(n-1, t[:-1], g[:-1])
            else:
                res += create_playlist(n-1, t[:i] + t[i+1:], g[:i] + g[i+1:])
        
        return res

def create_playlist_memo(n, t, g):
    if n == 1:
        if t[0] == T:
            return 1
        else:
            return 0
    else:
        res = 0
        for i in range(n):
            if i == 0:
                if (n-1, tuple(t[1:]), tuple(g[1:])) not in memo:
                    memo[(n-1, tuple(t[1:]), tuple(g[1:]))] = create_playlist_memo(n-1, t[1:], g[1:])
                res += memo[(n-1, tuple(t[1:]), tuple(g[1:]))]
            elif i == n-1:
                if (n-1, tuple(t[:-1]), tuple(g[:-1])) not in memo:
                    memo[(n-1, tuple(t[:-1]), tuple(g[:-1]))] = create_playlist_memo(n-1, t[:-1], g[:-1])
                res += memo[(n-1, tuple(t[:-1]), tuple(g[:-1]))]
            else:
                if (n-1, tuple(t[:i] + t[i+1:]), tuple(g[:i] + g[i+1:])) not in memo:
                    memo[(n-1, tuple(t[:i] + t[i+1:]), tuple(g[:i] + g[i+1:]))] = create_playlist_memo(n-1, t[:i] + t[i+1:], g[:i] + g[i+1:])
                res += memo[(n-1, tuple(t[:i] + t[i+1:]), tuple(g[:i] + g[i+1:]))]
        
        return res

def create_playlist_dp(n, t, g):
    dp = [[0 for i in range(T+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= t[i-1]:
                dp[i][j] += dp[i-1][j - t[i-1]]
    return dp[n][T]

def create_playlist_dp_memo(n, t, g):
    if (n, tuple(t), tuple(g)) in memo:
        return memo[(n, tuple(t), tuple(g))]
    
    dp = [[0 for i in range(T+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            if j >= t[i-1]:
                dp[i][j] += dp[i-1][j - t[i-1]]
    memo[(n, tuple(t), tuple(g))] = dp[n][T]
    return memo[(n, tuple(t), tuple(g))]

def create_playlist_dp_memo_optimized(n, t, g):
    if (n, tuple(t), tuple(g)) in memo:
