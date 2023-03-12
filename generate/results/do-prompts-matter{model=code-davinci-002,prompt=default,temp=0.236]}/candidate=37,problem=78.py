
# Solution

# This solution is based on the observation that the problem can be solved by dynamic programming.
# Let's define $dp[i][j]$ as the number of different sequences of songs, the total length of which is exactly $i$,
# such that there are no two consecutive songs of the same genre in them and all the songs in the playlist are different.
# The answer to the problem is $dp[T][0] + dp[T][1] + dp[T][2]$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j$,
# then the last song in the sequence can be any song with genre $j$ and duration $i$ (if such a song exists).
# Thus, $dp[i][j] = \sum\limits_{k=1}^n dp[i - t_k][j]$, where $t_k$ is the duration of the $k$-th song and $g_k = j$.
#
# Now let's find the recurrence relation for $dp[i][j]$.
# If we have a sequence of songs, the total length of which is exactly $i$, and the last song in the sequence has genre $j