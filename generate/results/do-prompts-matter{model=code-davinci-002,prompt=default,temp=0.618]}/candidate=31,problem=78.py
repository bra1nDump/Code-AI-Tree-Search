
"""

"""

import sys

def main(args):
    # Read file
    filename = "input_playlist.txt"
    if (len(args) > 1):
        filename = args[1]
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Parse input
    # t = int(lines[0])
    # for case in range(t):
    #     n, m = (int(x) for x in lines[case+1].split(' '))
    #     seq = [int(x) for x in lines[case+2].split(' ')]

    n, t = (int(x) for x in lines[0].split(' '))
    songs = []
    for i in range(n):
        songs.append(tuple(int(x) for x in lines[i+1].split(' ')))
    # print(songs)

    # Solve problem
    # print(songs[0][0])
    # print(songs[0][1])

    dp = [0] * (t+1)
    # print(dp)
    dp[0] = 1
    for i in range(1, t+1):
        for song in songs:
            print(dp)
            if (i - song[0] >= 0):
                dp[i] += dp[i-song[0]]
    print(dp)


if True:
    main(sys.argv)