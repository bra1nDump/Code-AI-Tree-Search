
n, T = map(int, input().split())

# we need to find all combinations of n songs that add up to exactly T minutes
# and are unique

# there are 3^n possible combinations, but we need just the ones that add up to
# T minutes

# This is the same as the coin change problem, except we have 3 different coins
# of different values. We need to find the number of ways to make a change of T
# units using the coins 1, 2, and 3.

# we can use a bottom up approach to build the table

# we need to find all combinations of n songs that add up to exactly T minutes
# and are unique

# there are 3^n possible combinations, but we need just the ones that add up to
# T minutes

# This is the same as the coin change problem, except we have 3 different coins
# of different values. We need to find the number of ways to make a change of T
# units using the coins 1, 2, and 3.

# we can use a bottom up approach to build the table

# initialize table
table = [[0 for i in range(T+1)] for j in range(n)]

# base case:
# 1 way to make change for 0, regardless of number of coins
for i in range(n):
    table[i][0] = 1

# iterate through each row (each coin)
for i in range(n):

    # iterate through each column (each change value)
    for j in range(T+1):

        # number of ways to make change for j, using i coins is equal to
        # number of ways to make change for j, using i coins, plus
        # number of ways to make change for j-value of coin, using i-1 coins
        if i > 0:
            table[i][j] = table[i-1][j]
        if j >= 1:
            table[i][j] += table[i][j-1]


print(table[-1][-1])