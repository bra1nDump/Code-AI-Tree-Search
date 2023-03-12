
# SOLUTION
import sys

# Read the input
n, T = map(int, sys.stdin.readline().split())

# Initialize the songs
songs = []
for i in range(n):
    songs.append(sys.stdin.readline().split())

# Initialize the songs that have the same length as the total time
songs_T = []
for i in range(n):
    if int(songs[i][0]) == T:
        songs_T.append(songs[i][1])

# Initialize the songs that have a length smaller than the total time
songs_0 = []
for i in range(n):
    if int(songs[i][0]) < T:
        songs_0.append(songs[i][1])

# Initialize the number of possible playlists
playlists = 0

# If there are songs with the same length as the total time
if len(songs_T) > 0:
    # Initialize the number of possible playlists
    playlists = 1
    # For each song with the same length as the total time
    for i in range(len(songs_T)):
        # Initialize the number of possible playlists
        playlists_i = 0
        # For each song with a length smaller than the total time
        for j in range(len(songs_0)):
            # If the song has a different genre
            if int(songs_0[j]) != int(songs_T[i]):
                playlists_i += 1
        playlists *= playlists_i

# If there are no songs with the same length as the total time
else:
    # Initialize the number of possible playlists
    playlists = 1
    # Initialize the number of songs with a length smaller than the total time
    songs_0_n = 0
    # For each song with a length smaller than the total time
    for i in range(len(songs_0)):
        # Initialize the number of songs with a length smaller than the total time
        songs_0_n_i = 0
        # For each song with a length smaller than the total time
        for j in range(len(songs_0)):
            # If the song has a different genre
            if int(songs_0[i]) != int(songs_0[j]):
                songs_0_n_i += 1
        playlists *= songs_0_n_i
        songs_0_n += 1
    playlists *= songs_0_n

# Print the number of possible playlists
print(playlists % 1000000007)