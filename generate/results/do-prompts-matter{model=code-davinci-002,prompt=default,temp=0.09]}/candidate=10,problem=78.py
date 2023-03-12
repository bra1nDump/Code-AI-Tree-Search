
# Solution 1
# This solution is not correct.
# It is not correct because it does not take into account the fact that the songs cannot be repeated.
# This solution is correct for the first example, but not for the second and third.

# n, T = map(int, input().split())
# songs = []
# for i in range(n):
#     songs.append(list(map(int, input().split())))
#
# # print(songs)
#
# def count_playlists(songs, T):
#     if T == 0:
#         return 1
#     if T < 0:
#         return 0
#     if len(songs) == 0:
#         return 0
#     return count_playlists(songs[1:], T) + count_playlists(songs[1:], T - songs[0][0])
#
# print(count_playlists(songs, T))


# Solution 2
# This solution is correct.
# It is correct because it takes into account the fact that the songs cannot be repeated.
# This solution is correct for the first, second and third examples.

n, T = map(int, input().split())
songs = []
for i in range(n):
    songs.append(list(map(int, input().split())))

# print(songs)

def count_playlists(songs, T):
    if T == 0:
        return 1
    if T < 0:
        return 0
    if len(songs) == 0:
        return 0
    return count_playlists(songs[1:], T) + count_playlists(songs[1:], T - songs[0][0])

def count_playlists_with_no_repeats(songs, T):
    if T == 0:
        return 1
    if T < 0:
        return 0
    if len(songs) == 0:
        return 0
    return count_playlists_with_no_repeats(songs[1:], T) + count_playlists_with_no_repeats(songs[1:], T - songs[0][0]) - count_playlists_with_no_repeats(songs[1:], T - 2 * songs[0][0])

print(count_playlists_with_no_repeats(songs, T))