
import sys

def main():
    # Read the input
    n, T = map(int, sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(list(map(int, sys.stdin.readline().split())))

    # Create a list of songs for each genre
    genre = [[] for i in range(4)]
    for i in range(n):
        genre[songs[i][1]].append(songs[i][0])

    # Create a list of all possible playlists
    playlists = []
    for i in range(1, 4):
        playlists.append(genre[i])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        playlists.append([genre[i], genre[j], genre[k]])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        for l in range(1, 4):
                            if i != l and j != l and k != l:
                                playlists.append([genre[i], genre[j], genre[k], genre[l]])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        for l in range(1, 4):
                            if i != l and j != l and k != l:
                                for m in range(1, 4):
                                    if i != m and j != m and k != m and l != m:
                                        playlists.append([genre[i], genre[j], genre[k], genre[l], genre[m]])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        for l in range(1, 4):
                            if i != l and j != l and k != l:
                                for m in range(1, 4):
                                    if i != m and j != m and k != m and l != m:
                                        for n in range(1, 4):
                                            if i != n and j != n and k != n and l != n and m != n:
                                                playlists.append([genre[i], genre[j], genre[k], genre[l], genre[m], genre[n]])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        for l in range(1, 4):
                            if i != l and j != l and k != l:
                                for m in range(1, 4):
                                    if i != m and j != m and k != m and l != m:
                                        for n in range(1, 4):
                                            if i != n and j != n and k != n and l != n and m != n:
                                                for o in range(1, 4):
                                                    if i != o and j != o and k != o and l != o and m != o and n != o:
                                                        playlists.append([genre[i], genre[j], genre[k], genre[l], genre[m], genre[n], genre[o]])

    # Create a list of all possible playlists
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                for k in range(1, 4):
                    if i != k and j != k:
                        for l in range(1, 4):
                            if i != l and j !=