
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def read_tuple():
    return tuple(read_ints())

def read_int():
    return read_ints()[0]

def main():
    n, T = read_tuple()
    songs = list()
    for i in range(n):
        songs.append(read_tuple())
    
    # dp[i][j][k] = number of ways to get to T minutes with i songs, last song is j, last song was of genre k
    # for k in range(4):
    #     dp[0][0][k] = 0
    #     dp[0][1][k] = 0
    #     dp[0][2][k] = 0
    #     dp[0][3][k] = 0
    # dp[0][0][0] = 1
    dp = [[[0] * 4 for _ in range(4)] for _ in range(T + 1)]
    dp[0][0][0] = 1

    for i in range(T):
        for j in range(n):
            for k in range(4):
                if k != 0:
                    dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k - 1]) % (10 ** 9 + 7)
                if k != songs[j][1]:
                    dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % (10 ** 9 + 7)
                if i + 1 >= songs[j][0]:
                    dp[i + 1][j][songs[j][1]] = (dp[i + 1][j][songs[j][1]] + dp[i + 1 - songs[j][0]][j][k]) % (10 ** 9 + 7)

    print(sum(dp[T][i][0] for i in range(n)))

def test():
    assert(main() == None)

if True:
    test()