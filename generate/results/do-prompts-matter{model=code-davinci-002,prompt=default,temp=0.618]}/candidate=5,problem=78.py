
# SOLUTION
# This problem is similar to the problem of finding the number of subsets with a given sum.
# The problem is reduced to the problem of finding the number of subsets with a given sum.

# Dynamic programming solution.

def find_subsets(A, genre, T):
    # A - list of songs
    # genre - genre of the last song
    # T - required total duration

    # Create two arrays, one for the current song and one for the previous song.
    # Create a two-dimensional array to store the number of subsets with a given sum.
    # Initialize array elements to zero.
    N = len(A)
    cur = [0 for i in range(T+1)]
    prev = [0 for i in range(T+1)]
    prev[0] = 1

    for i in range(N):
        for j in range(T+1):
            if A[i][1] == genre:
                if j < A[i][0]:
                    cur[j] = prev[j]
                else:
                    cur[j] = prev[j] + prev[j-A[i][0]]
            else:
                cur[j] = prev[j]

        for j in range(T+1):
            prev[j] = cur[j]

    return cur[T]

# Main function.
n, T = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# Find the number of subsets with a sum of T, considering the last song of each genre.
# The result is the sum of the results.
print(find_subsets(A, 1, T) + find_subsets(A, 2, T) + find_subsets(A, 3, T))