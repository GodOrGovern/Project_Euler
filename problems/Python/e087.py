''' How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power? '''

from itertools import product
from primesieve.numpy import primes as primes_to

def main():
    ''' Driver function '''
    prime = primes_to(7072)
    prime = [prime, prime[prime < 369], prime[prime < 85]]
    vals = set()
    for p in product(*prime):
        val = p[0]**2 + p[1]**3 + p[2]**4
        if val < 5e7:
            vals.add(val)
    print(len(vals))

if __name__ == "__main__":
    main()
