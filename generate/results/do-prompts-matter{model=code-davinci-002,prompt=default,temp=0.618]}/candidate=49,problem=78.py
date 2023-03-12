
def main():
    num_songs, total_duration = map(int, input().split())
    songs = [tuple(map(int, input().split())) for i in range(num_songs)]

    def num_playlists(songs, total_duration):
        if total_duration == 0: return 1

        if songs == []: return 0

        if (songs, total_duration) in memo: return memo[(songs, total_duration)]

        num_playlists_without = num_playlists(songs[1:], total_duration)
        num_playlists_with = 0

        if total_duration - songs[0][0] >= 0:
            num_playlists_with = num_playlists(songs[1:], total_duration - songs[0][0])

        memo[(songs, total_duration)] = num_playlists_without + num_playlists_with
        return memo[(songs, total_duration)]

    memo = {}
    answer = num_playlists(songs, total_duration)
    print(answer)

if True:
    main()