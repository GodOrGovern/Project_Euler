''' A composite is a number containing at least two prime factors. How many
composite integers, n < 10^8, have precisely two, not necessarily distinct,
prime factors? '''

from bisect import bisect
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    print(semiprime_below(10**8))

def semiprime_below(end):
    ''' Determine how many semiprimes are below 'end' '''
    total = 0
    primes = primes_to(end)
    for i, p in enumerate(primes[:bisect(primes, int(end**0.5))]):
        total += bisect(primes, end//p) - i
    return total

if __name__ == "__main__":
    main()
