''' Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (p_n−1)^n + (p_n+1)^n is divided by p_n^2. Find the least value of n for which the remainder first exceeds 10^10 '''

from itertools import count
from pyprimesieve import primes_nth

def main():
    ''' Driver function '''
    for n in count(1, 1):
        p = primes_nth(n)
        p_sqr = p**2
        rem = (pow(p-1, n, p_sqr) + pow(p+1, n, p_sqr)) % p_sqr
        if rem > 10**10:
            print(n)
            break

if __name__ == "__main__":
    main()