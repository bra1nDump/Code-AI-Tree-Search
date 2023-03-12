
# Solution #

# This problem can be solved using Dynamic Programming.
# Let's define some values.
# totalSongs = n
# totalDuration = T
# songDuration = t
# songGenre = g
# songs = list of songs
# playlist = list of songs in the playlist

# Let's define some states.
# state = [i,t,g]
# i = current song index
# t = total duration of the current playlist
# g = last genre in the playlist

# Let's define the transition function.
# f(i,t,g) = f(i+1,t,g) + f(i+1,t+ti,gi)
# The first step is to check if the current song can be added to the playlist.
# This can be done by comparing the total duration of the current playlist + current song duration to the total duration.
# The second step is to check if the last genre in the playlist is the same as the current song genre. If it is, then the current song cannot be added to the playlist.
# The third step is to check if the current song has already been added to the playlist.

# Let's define the base case.
# f(i,t,g) = 0 if i > n

# Let's define the final state.
# f(n,T,g)

# Let's create the memo table (list of lists).
# memo = [[[0 for i in range(4)] for j in range(T+1)] for k in range(n+1)]

# Let's create the function.
def createPlaylist(songs, totalDuration):
    """
    The function returns the number of different sequences of songs, the total length of exactly totalDuration, such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different.
    """
    totalSongs = len(songs)
    memo = [[[0 for i in range(4)] for j in range(totalDuration+1)] for k in range(totalSongs+1)]
    def f(i,t,g):
        if i > totalSongs:
            return 0
        elif memo[i][t][g] > 0:
            return memo[i][t][g]
        else:
            if t + songs[i-1][0] <= totalDuration and g != songs[i-1][1]:
                memo[i][t][g] = f(i+1,t,g) + f(i+1,t+songs[i-1][0],songs[i-1][1])
            else:
                memo[i][t][g] = f(i+1,t,g)
            return memo[i][t][g]
    return f(1,0,0)

# Let's test the function.
songs1 = [[1,1],[1,2],[1,3]]
print(createPlaylist(songs1,3))

songs2 = [[1,1],[1,1],[1,3]]
print(createPlaylist(songs2,3))

songs3 = [[5,3],[2,1],[3,2],[5,1]]
print(createPlaylist(songs3,10))