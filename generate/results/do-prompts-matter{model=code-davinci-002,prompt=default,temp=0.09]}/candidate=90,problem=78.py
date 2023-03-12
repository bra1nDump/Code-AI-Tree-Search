
# Solution

# This solution is based on the idea of dynamic programming.
# We will use a 3D array to store the number of playlists of length i,
# ending with a song of genre j, and with a total duration of k.
# We will then use this array to calculate the number of playlists of length i+1,
# ending with a song of genre j, and with a total duration of k.
# The number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# is equal to the sum of the number of playlists of length i, ending with a song of genre j, and with a total duration of k-t,
# for all t in the range [1, 15].
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k.
# We will then subtract the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# from the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j-1.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j+1.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j+2.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j-2.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j+3.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j-3.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j+4.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j-4.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
# if the song of genre j is the same as the song of genre j+5.
# We will then add the number of playlists of length i, ending with a song of genre j, and with a total duration of k,
# to the number of playlists of length i+1, ending with a song of genre j, and with a total duration of k,
