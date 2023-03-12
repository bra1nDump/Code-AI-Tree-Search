
def main():
    # Get input
    n, T = [int(x) for x in input().split()]
    songs = []
    for i in range(n):
        songs.append([int(x) for x in input().split()])
    # print(songs)

    # Get all possible playlists
    playlists = []
    for i in range(1, n+1):
        for p in itertools.permutations(songs, i):
            if sum([x[0] for x in p]) == T:
                playlists.append(p)
    # print(playlists)

    # Remove playlists with adjacent songs of the same genre
    for p in playlists:
        for i in range(len(p)-1):
            if p[i][1] == p[i+1][1]:
                playlists.remove(p)
                break
    # print(playlists)

    # Remove duplicates
    playlists = list(set(playlists))
    # print(playlists)

    # Print output
    print(len(playlists))

if True:
    main()