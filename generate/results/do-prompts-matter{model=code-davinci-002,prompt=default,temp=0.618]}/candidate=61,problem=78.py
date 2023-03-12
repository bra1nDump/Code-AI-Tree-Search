
# from math import prod

# def prod(iterable):
#     return reduce(operator.mul, iterable, 1)

def num_playlists(songs, total_time):
  """
  Dynamic programming solution.
  """
  # Sort songs by length.
  songs.sort()
  # Init DP array.
  arr = [[0] * (total_time + 1) for _ in range(len(songs))]
  # Fill in first row.
  song_length = songs[0][0]
  song_genre = songs[0][1]
  # Fill in first row.
  arr[0][song_length] = 1
  # Fill in first column.
  for i in range(1, len(songs)):
    if songs[i][1] != song_genre:
      arr[i][0] = 1
  # Fill in rest of DP array.
  for i in range(1, len(songs)):
    for j in range(total_time + 1):
      song_length = songs[i][0]
      song_genre = songs[i][1]
      # Add up all valid playlists with current song at the end.
      for k in range(j - song_length, -1, -1):
        if songs[i-1][1] != song_genre:
          arr[i][j] += arr[i-1][k]
      # Add up all valid playlists without current song at the end.
      arr[i][j] += arr[i-1][j]
  # Return last element.
  return arr[len(songs)-1][total_time]


def num_playlists2(songs, total_time):
  """
  Recursive solution.
  """
  def helper(songs, total_time, last_genre):
    # Base cases.
    if total_time < 0:
      return 0
    if total_time == 0:
      return 1
    # Init result.
    result = 0
    for i in range(len(songs)):
      # If song and last song are not of same genre.
      if songs[i][1] != last_genre:
        # Recurse.
        result += helper(songs, total_time - songs[i][0], songs[i][1])
    return result
  # Init cache.
  cache = {}
  # Recurse.
  return helper(songs, total_time, 0)

def main():
  # Get input.
  n, T = [int(x) for x in input().split()]
  songs = []
  for _ in range(n):
    song = [int(x) for x in input().split()]
    songs.append(song)
  # Compute and print result.
  print(num_playlists2(songs, T))

if True:
  main()