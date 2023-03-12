
def create_prefix_sums(n, lst):
    prefix_sums = []
    prefix_sums.append(lst[0])
    for i in range(1, len(lst)):
        prefix_sums.append(prefix_sums[i-1] + lst[i])
    return prefix_sums

def find_index(prefix_sums, target):
    l = 0
    r = len(prefix_sums) - 1
    while l <= r:
        mid = (l + r) // 2
        if prefix_sums[mid] == target:
            return mid
        elif prefix_sums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

def get_valid_subsets(n, m, songs, prefix_sums, target):
    total = 0
    for i in range(m):
        index = find_index(prefix_sums[i], target)
        if index == n:
            break
        if index == 0:
            continue
        if songs[i][1] != songs[index][1]:
            total += 1
    return total

def main():
    n, m = list(map(int, input().split()))
    songs = []
    for i in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort()
    prefix_sums = []
    for i in range(3):
        prefix_sums.append(create_prefix_sums(n, [song[0] for song in songs if song[1] == i+1]))
    
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if songs[i][1] != songs[j][1] and songs[j][1] != songs[k][1] and songs[i][1] != songs[k][1]:
                    total += get_valid_subsets(n, m, songs, prefix_sums, m - (songs[i][0] + songs[j][0] + songs[k][0]))

    print(total)

if True:
    main()