
import sys

def main():
    n, T = (int(x) for x in sys.stdin.readline().split())
    songs = []
    for i in range(n):
        songs.append(tuple(int(x) for x in sys.stdin.readline().split()))
    songs.sort()
    choices = {}
    for t, g in songs:
        if (t, g) in choices:
            continue
        choices[t, g] = 1
        for tt, gg in choices:
            if tt + t <= T and gg != g:
                choices[tt + t, g] = choices.get((tt + t, g), 0) + choices[tt, gg]
    print(sum(choices.get((T, g), 0) for g in range(1, 4)))

main()