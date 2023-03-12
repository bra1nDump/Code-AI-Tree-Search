from collections import defaultdict
from math import factorial

mod = 10**9 + 7

# def generate_playlists(songs, t):
# 	if t == 0:
# 		return 1
# 	if len(songs) == 0:
# 		return 0
# 	playlists = 0
# 	for i, song in enumerate(songs):
# 		if song[0] <= t:
# 			playlists += generate_playlists(songs[i+1:], t-song[0])
# 	return playlists

# def generate_playlists(songs, t):
# 	if t == 0:
# 		return 1
# 	if len(songs) == 0:
# 		return 0
# 	playlists = 0
# 	for i, song in enumerate(songs):
# 		if song[0] <= t:
# 			playlists += generate_playlists(songs[i+1:], t-song[0])
# 	return playlists

def playlists(n, t, songs):
	if t == 0:
		return 1
	if n == 0:
		return 0
	playlists = 0
	# for i, song in enumerate(songs):
	# 	if song[0] <= t:
	# 		playlists += generate_playlists(songs[i+1:], t-song[0])
	for i in range(n):
		if songs[i][0] <= t:
			playlists += playlists(n-1, t-songs[i][0], songs[:i]+songs[i+1:])
	return playlists

def main():
	n, t = map(int, input().split())
	songs = []
	for _ in range(n):
		t_i, g_i = map(int, input().split())
		songs.append([t_i, g_i])
	songs.sort(key=lambda song: song[0])
	playlists = 0
	for i, song in enumerate(songs):
		if song[0] <= t:
			playlists += playlists(n-1, t-song[0], songs[:i]+songs[i+1:])
	print(playlists)

if True:
	main()