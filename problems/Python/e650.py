''' Let B(n) = the product of (n choose k) with k = 0 to n. Let D(n) = the sum
of the divisors of B(n). Let S(n) = the sum of D(k) with k = 1 to n. Find
S(20000) mod 1000000007 '''

from collections import defaultdict
from pyprimesieve import factorize

def main():
    ''' Driver function '''
    end = 20000
    mod = 10**9 + 7
    facs = factorial_factors(end+1)
    binomials = binomial_prod(facs)
    print(div_sum(binomials, mod, end) + 1)

def factorial_factors(end):
    ''' Returns dict of prime factors of factorials from 1 to 'end' '''
    factors = {1: {}}
    for n in range(2, end):
        factors[n] = defaultdict(int)
        for p, e in factors[n-1].items():
            factors[n][p] = e
        for p, e in factorize(n):
            factors[n][p] += e
    del factors[1]
    return factors

def binomial_prod(factors):
    ''' Return dict of prime factors of binomial products '''
    superfacs = {1: {}}
    binomials = dict()
    for n, facs in factors.items():
        superfacs[n] = defaultdict(int)
        binomials[n] = defaultdict(int)
        for p, e in facs.items():
            superfacs[n][p] = e
            binomials[n][p] = e*(n - 1)
        for p, e in superfacs[n-1].items():
            superfacs[n][p] += e
            binomials[n][p] -= 2*e
    return binomials

def div_sum(factors, mod, end):
    ''' Sum of divisors of 'factors' modulo 'mod', where 'mod' is prime '''
    result = 0
    for n in range(2, end+1):
        numer, denom = 1, 1
        for p, e in factors[n].items():
            numer = numer * (pow(p, e+1, mod)-1) % mod
            denom = denom * (p - 1) % mod
        result += numer*pow(denom, mod-2, mod) % mod
    return result % mod

if __name__ == "__main__":
    main()
