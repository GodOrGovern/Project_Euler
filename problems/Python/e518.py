''' Let S(n) = Σa+b+c over all triples (a,b,c) such that: a, b, and c are prime
numbers; a < b < c < n; a+1, b+1, and c+1 form a geometric sequence. Find
S(10**8) '''

from math import ceil, isqrt
from pyprimesieve import factorize
from pyprimesieve import primes as primes_to

def main():
    ''' Takes about a minute to finish running '''
    print(S(10**8))

def S(n):
    ''' Implementation of the S(n) function described above '''
    n_sqr = n*n
    total = 0
    primes = primes_to(n)
    primes_set = set(primes)
    for i, a in enumerate(primes):
        # m is an integer such that if f(x) = (x*m)**2 for any natural x, f(x)
        # returns the xth perfect square divisible by a+1
        # From: https://math.stackexchange.com/a/4084884/530956
        m = 1
        for p, e in factorize(a+1):
            m *= p**(ceil(e/2))
        m_sqr = m*m
        x = a//n
        val = m_sqr // (a+1)
        c = x*x*val-1
        while (c := c + val*(2*x+1)) < n:
            x += 1
            if (c in primes_set) and ((b := x*m-1) in primes_set) and (a < b < c):
                total += a + b + c
    return total

if __name__ == "__main__":
    main()
