''' A unitary divisor d of a number n is a divisor of n that has the property
gcd(d, n/d) = 1. Let S(n) represent the sum of the squares of the unitary
divisors of n. Find S(100,000,000!) modulo 1,000,000,009 '''

from pyprimesieve import primes

def main():
    ''' Driver function '''
    end = 10**8
    total = 1
    mod = 10**9 + 9
    powers = prime_powers(end)
    for p, e in powers.items():
        total = total * (pow(p, 2*e, mod)+1) % mod
    print(total)

def prime_powers(n):
    ''' Return dict where keys are primes and values are exponents. Represents
    prime factorization of 'n!' '''
    powers = dict()
    for p in primes(n):
        powers[p] = legendre(p, n)
    return powers

def legendre(p, n):
    ''' Implementation of Legendre's formula. Finds the largest 'exp' so that
    'p**exp' still divides 'n!'. 'p' is assumed to be prime '''
    exp, i, div = 0, 1, 1
    while div:
        div = n // p**i
        exp += div
        i += 1
    return exp

if __name__ == "__main__":
    main()
