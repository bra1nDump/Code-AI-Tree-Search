
import sys

def read_int():
    return int(sys.stdin.readline().strip())

def read_int_n_list():
    return [int(n) for n in sys.stdin.readline().split()]


def main():
    n, t = read_int_n_list()
    songs = []
    for i in range(n):
        songs.append(read_int_n_list())

    dp = [0] * (t+1)
    for i in range(1, t+1):
        for j in range(n):
            if songs[j][0] == i:
                dp[i] += 1
            if songs[j][0] < i:
                dp[i] += dp[i-songs[j][0]]
    print(dp[t])


if True:
    main()