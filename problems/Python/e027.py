''' Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0 '''

from sympy import isprime

def main():
    ''' Driver function '''
    coef = find_coef()
    print(coef[0]*coef[1])

def find_coef():
    ''' Check all valid combinations of coefficients and find number of
    consecutive primes produced by each combination '''
    max_prime = 0
    coef = []
    for a in range(-999, 1000):
        for b in range(1001):
            n = 0
            while isprime(n**2 + a*n + b):
                n += 1
            if n > max_prime:
                max_prime = n
                coef = [a, b]
    return coef

if __name__ == "__main__":
    main()
