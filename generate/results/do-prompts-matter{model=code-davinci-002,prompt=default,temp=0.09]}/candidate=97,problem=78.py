
# Solution 1
# This solution is based on the observation that the number of playlists of length $T$ is equal to the sum of the number of playlists of length $T-t_i$ for all $i$ such that $t_i \le T$.
# This is because we can append any song of length $t_i$ to any playlist of length $T-t_i$ to get a playlist of length $T$.
# This is a recursive solution, but we can use memoization to make it run in $O(nT)$ time.
# The base case is when $T=0$, in which case there is only one playlist of length $0$, which is the empty playlist.
# The recursive case is when $T>0$, in which case we can add any song of length $t_i$ to any playlist of length $T-t_i$ to get a playlist of length $T$.
# We can use memoization to store the number of playlists of length $T$ for each $T$ in a list.
# We can also use memoization to store the number of playlists of length $T$ for each $T$ and each genre $g$ in a dictionary.
# This is because we can't have two consecutive songs of the same genre, so we need to keep track of the genre of the last song in the playlist.
# We can use the same idea to keep track of the last two songs in the playlist, but this is not necessary.
# The time complexity is $O(nT)$ and the space complexity is $O(nT)$.

def numPlaylists(n, T, songs):
    # Initialize the memoization lists.
    # The first list stores the number of playlists of length $T$ for each $T$.
    # The second list stores the number of playlists of length $T$ for each $T$ and each genre $g$.
    # The base case is when $T=0$, in which case there is only one playlist of length $0$, which is the empty playlist.
    # The recursive case is when $T>0$, in which case we can add any song of length $t_i$ to any playlist of length $T-t_i$ to get a playlist of length $T$.
    # We can use memoization to store the number of playlists of length $T$ for each $T$ in a list.
    # We can also use memoization to store the number of playlists of length $T$ for each $T$ and each genre $g$ in a dictionary.
    # This is because we can't have two consecutive songs of the same genre, so we need to keep track of the genre of the last song in the playlist.
    # We can use the same idea to keep track of the last two songs in the playlist, but this is not necessary.
    # The time complexity is $O(nT)$ and the space complexity is $O(nT)$.
    playlists = [1] + [0] * T
    playlistsByGenre = [{} for _ in range(T+1)]
    playlistsByGenre[0][0] = 1
    for t in range(1, T+1):
        for i in range(n):
            t_i, g_i = songs[i]
            if t_i <= t:
                playlists[t] += playlists[t-t_i]
                for g in playlistsByGenre[t-t_i]:
                    if g != g_i:
                        if g_i not in playlistsByGenre[t]:
                            playlistsByGenre[t][g_i] = 0
                        playlistsByGenre[t][g_i] += playlistsByGenre[t-t_i][g]
    return playlists[T]

# Solution 2
# This solution is based on the observation that the number of playlists of length $T$ is equal to the sum of the number of playlists of length $T-t_i$ for all $i$ such that $t_i \le T$.
# This is because we can append any song of length $t_i$ to any playlist of length $T-t_i$ to get a playlist of length $T$.
# This is a recursive solution, but we can use memoization to make it run in $O(nT)$ time.
# The base case is when $T=0$, in which case there is only one playlist of length $0$, which is the empty playlist.
