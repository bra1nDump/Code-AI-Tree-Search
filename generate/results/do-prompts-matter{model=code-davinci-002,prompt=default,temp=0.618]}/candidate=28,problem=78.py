
def mod_pow(x, y, mod):
    """
    x**y % mod
    """
    if y == 0:
        return 1 % mod
    if y == 1:
        return x % mod
    if y % 2 == 0:
        z = mod_pow(x, y//2, mod)
        return (z*z) % mod
    else:
        return (x*mod_pow(x, y-1, mod)) % mod

def div_mod(x, y, mod):
    """
    x / y % mod
    """
    return (x*mod_pow(y, mod-2, mod)) % mod

def choose(n, k, mod):
    """
    nCk % mod
    """
    ans = 1
    for i in range(k):
        ans = (ans*(n-i)) % mod
    for i in range(1, k+1):
        ans = div_mod(ans, i, mod)
    return ans

def solve(n, T, S):
    # The number of ways to pick T songs of length S
    # is the number of ways to pick (T-1) songs of length (S-1)
    # with the last song having length 1
    # plus the number of ways to pick T songs of length (S-1)
    # with the last song having length 2
    # plus the number of ways to pick T songs of length (S-1)
    # with the last song having length 3
    # plus the number of ways to pick T songs of length (S-1)
    # with the last song having length 4
    # ...
    # plus the number of ways to pick T songs of length (S-1)
    # with the last song having length 15
    #
    # So, we want to count the number of ways to pick (T-1) songs
    # of length (S-1).
    # The answer to that is the number of ways to pick (T-1) songs
    # of length (S-2).
    #
    # So, we want the number of ways to pick (T-1) songs of length (S-2).
    # This is the number of ways to pick (T-2) songs of length (S-2)
    # with the last song having length 1
    # ...
    # plus the number of ways to pick (T-1) songs of length (S-2)
    # with the last song having length (T-1)
    # ...
    # plus the number of ways to pick (T-1) songs of length (S-2)
    # with the last song having length 15
    #
    # So, we want to count the number of ways to pick (T-2) songs
    # of length (S-2).
    # The answer to that is the number of ways to pick (T-3) songs
    # of length (S-2).
    #
    # So, we want the number of ways to pick (T-3) songs of length (S-2).
    # This is the number of ways to pick (T-3) songs of length (S-3)
    # with the last song having length 1
    # ...
    # plus the number of ways to pick (T-3) songs of length (S-2)
    # with the last song having length (T-3)
    # ...
    # plus the number of ways to pick (T-3) songs of length (S-2)
    # with the last song having length 15
    #
    # ...
    #
    # So, we want the number of ways to pick (T-4) songs of length (S-2).
    # This is the number of ways to pick (T-4) songs of length (S-3)
    # with the last song having length 1
    # ...
    # plus the number of ways to pick (T-4) songs of length (S-2)
    # with the last song having length (T-4)
    # ...
    # plus the number of ways to pick (T-4) songs of length (S-2)
    # with the last song having length 15
    #
    # ...
    #
    # So, we want the number of ways to pick (T-5) songs of length (S-2).
    # This is the number of