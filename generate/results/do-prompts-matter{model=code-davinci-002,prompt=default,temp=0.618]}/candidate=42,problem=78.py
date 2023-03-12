
import math
import sys

mod = 10**9 + 7

def input():
    return sys.stdin.readline()

def get_input(n):
    arr = [int(i) for i in input().split()]
    return arr[:n]

def get_n_input(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))
    return arr

def print_dp(dp):
    for row in dp:
        print(row)

def dp(arr, n, t):
    # dp[i][j][k] is the number of ways to make a playlist of length j,
    # ending with song i, genre k
    dp = [[[0 for i in range(3)] for i in range(t+1)] for i in range(n)]
    # dp[i][j] is the number of ways to make a playlist of length j,
    # ending with song i
    dp2 = [[0 for i in range(t+1)] for i in range(n)]

    for i in range(n):
        # initialize the first song
        dp[i][arr[i][0]][arr[i][1]-1] = 1
        dp2[i][arr[i][0]] = 1
        for j in range(t+1):
            for k in range(3):
                if j-arr[i][0] >= 0:
                    # add the current song to a playlist that ends with
                    # song i-1, genre k
                    dp[i][j][k] = dp[i-1][j-arr[i][0]][k]
                    # add the current song to a playlist that ends with
                    # song i-1
                    dp2[i][j] += dp2[i-1][j-arr[i][0]]
                    if k != arr[i][1]-1:
                        # add the current song to a playlist that ends with
                        # song i-1, genre k, and subtract the song after the
                        # current song is the same genre
                        dp[i][j][k] -= dp[i-1][j-arr[i][0]-arr[i][0]][arr[i][1]-1]
                        # add the current song to a playlist that ends with
                        # song i-1, and subtract the song after the
                        # current song is the same genre
                        dp2[i][j] -= dp2[i-1][j-arr[i][0]-arr[i][0]]
                    dp[i][j][k] %= mod
                    dp2[i][j] %= mod
    #print_dp(dp)
    #print('')
    #print_dp(dp2)
    return dp2[n-1][t]

n, t = get_input(2)
arr = []
for i in range(n):
    arr.append(get_input(2))

print(dp(arr, n, t))