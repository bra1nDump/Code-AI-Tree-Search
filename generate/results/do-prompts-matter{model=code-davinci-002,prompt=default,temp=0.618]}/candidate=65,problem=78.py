

def solve(n, T, songs):
    """
    Use dynamic programming to solve the problem
    """
    # Initialize the list of lists
    # dp[i][j] - list containing all the ways to sum up to i with songs of length up to j
    dp = [[[] for _ in range(T + 1)] for _ in range(n + 1)]

    # Initialize the base case
    dp[0][0] = [[]]

    # Iterate through all songs
    for i in range(1, n + 1):
        # Iterate through all lengths
        for j in range(T + 1):
            # If current song length fits
            if j >= songs[i][0]:
                # If previous song has the same genre
                if i > 1 and songs[i][1] == songs[i - 1][1]:
                    for k in range(j - songs[i][0] + 1):
                        for lst in dp[i - 1][k]:
                            dp[i][j].append(lst + [i])
                # If previous song has a different genre
                else:
                    for k in range(j - songs[i][0] + 1):
                        for lst in dp[i - 1][k] + dp[i - 2][k]:
                            dp[i][j].append(lst + [i])
            # If current song length doesn't fit
            else:
                # If previous song has the same genre
                if i > 1 and songs[i][1] == songs[i - 1][1]:
                    for lst in dp[i - 1][j]:
                        dp[i][j].append(lst + [i])
                # If previous song has a different genre
                else:
                    for lst in dp[i - 1][j] + dp[i - 2][j]:
                        dp[i][j].append(lst + [i])

    return dp[n][T]


def main():
    n, T = [int(x) for x in input().split()]
    songs = {i + 1: [int(x) for x in input().split()] for i in range(n)}

    result = solve(n, T, songs)

    print(len(result))


if True:
    main()