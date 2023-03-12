
import sys

# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n/2) if sieve[i]]

def get_divisors(n):
    divisors = [1]
    for prime in primes(n):
        if n % prime == 0:
            divisors.append(prime)
    return divisors

def get_all_divisors(n):
    divisors = [1]
    for prime in primes(n):
        if n % prime == 0:
            divisors.append(prime)
            divisors.append(n/prime)
    return divisors

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


MOD = 1000000007

def solve(args):
    """
    >>> solve([3, 3, 1, 1, 1, 2, 1, 3])
    6

    >>> solve([3, 3, 1, 1, 1, 1, 1, 3])
    2

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([4, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    10

    >>> solve([5, 10, 5, 3, 2, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1])
    20
    """

    # index 0: num_songs, 1: total_length, 2: song_length, 3: song_genre
    num_songs = args[0]
    total_length = args[1]
    song_length_genre = args[2:]

    #