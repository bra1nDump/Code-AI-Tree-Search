
import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))
    print(solve(n, T, songs))

def solve(n, T, songs):
    # dp[i][j] = number of ways to make a playlist of length j using the first i songs
    dp = [[0 for i in range(T+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(T+1):
            if j >= songs[i-1][0]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-songs[i-1][0]]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    # print(dp[n][T])
    # Now we need to subtract the number of ways to make a playlist of length T using the first n songs such that there are two consecutive songs of the same genre
    # We can do this by subtracting the number of ways to make a playlist of length T-1 using the first n songs such that there are two consecutive songs of the same genre
    # This is because we can add a song of length 1 to the end of any playlist of length T-1 such that there are two consecutive songs of the same genre
    # We can repeat this process until we get to the number of ways to make a playlist of length T-k using the first n songs such that there are two consecutive songs of the same genre
    # where k is the length of the longest song in the playlist
    # We can then subtract all of these numbers from the number of ways to make a playlist of length T using the first n songs
    # print(dp[n][T-1])
    # print(dp[n][T-2])
    # print(dp[n][T-3])
    # print(dp[n][T-4])
    # print(dp[n][T-5])
    # print(dp[n][T-6])
    # print(dp[n][T-7])
    # print(dp[n][T-8])
    # print(dp[n][T-9])
    # print(dp[n][T-10])
    # print(dp[n][T-11])
    # print(dp[n][T-12])
    # print(dp[n][T-13])
    # print(dp[n][T-14])
    # print(dp[n][T-15])
    # print(dp[n][T-16])
    # print(dp[n][T-17])
    # print(dp[n][T-18])
    # print(dp[n][T-19])
    # print(dp[n][T-20])
    # print(dp[n][T-21])
    # print(dp[n][T-22])
    # print(dp[n][T-23])
    # print(dp[n][T-24])
    # print(dp[n][T-25])
    # print(dp[n][T-26])
    # print(dp[n][T-27])
    # print(dp[n][T-28])
    # print(dp[n][T-29])
    # print(dp[n][T-30])
    # print(dp[n][T-31])
    # print(dp[n][T-32])
    # print(dp[n][T-33])
    # print(dp[n][T-34])
    # print(dp[n][T-35])
    # print(dp[n][T-36])
    # print(dp[n][T-37])
    # print(dp[n][T-38])
    # print(dp[n][T-39])
    # print(dp[n][T-40])
    # print(dp[n][T-41])
    # print(dp[n][T-42])
    # print(dp[n][T-43])
    #