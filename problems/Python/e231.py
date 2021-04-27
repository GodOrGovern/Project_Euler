''' Find the sum of the terms in the prime factorisation of 20*10**6 choose 15*10**6 '''

from pyprimesieve import primes

def main():
    ''' Driver function '''
    n, m = 20*10**6, 15*10**6
    total = 0
    for p in primes(n):
        total += p*(legendre(n,p)-legendre(m,p)-legendre(n-m,p))
    print(total)

def legendre(n, p):
    ''' Using Legendre's formula, return the highest exponent of the prime p
    that divides n! '''
    exp = 0
    pow_p = p
    while pow_p < n:
        exp += n // pow_p
        pow_p *= p
    return exp

if __name__ == "__main__":
    main()
