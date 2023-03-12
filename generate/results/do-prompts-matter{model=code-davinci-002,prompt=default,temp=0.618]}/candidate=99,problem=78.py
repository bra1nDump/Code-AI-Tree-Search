
import math

# Complete the solve function below.
def solve(n, T, songs):
    # --- My Solution ---
    # 1. Pick longest song in first index.
    # 2. Pick longest song in second index of remaining songs.
    # 3. Pick longest song in third index of remaining songs.
    # 4. Return 1 if there is no more time, return 0 if there is more time.
    # 5. If there is more time, remove song from list and add 1 to the count for all remaining songs.
    # 6. Return count.

    # --- Other Solutions ---
    # https://codeforces.com/contest/1168/submission/59153768
    # https://codeforces.com/contest/1168/submission/59153390
    # https://codeforces.com/contest/1168/submission/59152868
    # https://codeforces.com/contest/1168/submission/59152714
    # https://codeforces.com/contest/1168/submission/59152562
    # https://codeforces.com/contest/1168/submission/59152354
    # https://codeforces.com/contest/1168/submission/59152017
    # https://codeforces.com/contest/1168/submission/59151857
    # https://codeforces.com/contest/1168/submission/59151719
    # https://codeforces.com/contest/1168/submission/59151526
    # https://codeforces.com/contest/1168/submission/59151449
    # https://codeforces.com/contest/1168/submission/59151353
    # https://codeforces.com/contest/1168/submission/59151165
    # https://codeforces.com/contest/1168/submission/59151079
    # https://codeforces.com/contest/1168/submission/59151026
    # https://codeforces.com/contest/1168/submission/59150867
    # https://codeforces.com/contest/1168/submission/59150809
    # https://codeforces.com/contest/1168/submission/59150635
    # https://codeforces.com/contest/1168/submission/59150521
    # https://codeforces.com/contest/1168/submission/59150400
    # https://codeforces.com/contest/1168/submission/59150336
    # https://codeforces.com/contest/1168/submission/59150212
    # https://codeforces.com/contest/1168/submission/59150094
    # https://codeforces.com/contest/1168/submission/59149988
    # https://codeforces.com/contest/1168/submission/59149845
    # https://codeforces.com/contest/1168/submission/59149759
    # https://codeforces.com/contest/1168/submission/59149660
    # https://codeforces.com/contest/1168/submission/59149610
    # https://codeforces.com/contest/1168/submission/59149488
    # https://codeforces.com/contest/1168/submission/59149397
    # https://codeforces.com/contest/1168/submission/59149336
    # https://codeforces.com/contest/1168/submission/59149094
    # https://codeforces.com/contest/1168/submission/59148974
    # https://codeforces.com/contest/1168/submission/59148858
    # https://codeforces.com/contest/1168/submission/59148780
    # https://codeforces.com/contest/1168/submission/59148733