
def main():
    # Input
    n, T = map(int, input().split())
    song_list = []
    for i in range(n):
        t, g = map(int, input().split())
        song_list.append((t, g))

    # Generate all possible playlists
    playlist = []
    generate_playlist(song_list, playlist, T)

    # Check if playlist is valid
    valid_playlist = []
    for pl in playlist:
        if is_valid_playlist(pl):
            valid_playlist.append(pl)

    # Generate all possible playlists
    print(len(valid_playlist))

def generate_playlist(song_list, playlist, T):
    if len(song_list) == 0:
        return

    for i in range(len(song_list)):
        time = song_list[i][0]
        if T - time < 0:
            continue
        else:
            pl = []
            pl.append(i+1)
            if T - time == 0:
                playlist.append(pl)
            else:
                new_song_list = song_list[:i] + song_list[i+1:]
                generate_playlist(new_song_list, playlist, T - time)
                for s in playlist:
                    if is_valid_playlist(s):
                        pl += s
                        playlist.append(pl)
                playlist.remove(pl)

def is_valid_playlist(playlist):
    if len(playlist) == 1:
        return True

    for i in range(len(playlist) - 1):
        if playlist[i][1] == playlist[i+1][1]:
            return False
    return True

if True:
    main()