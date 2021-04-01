''' S(k) is the sum of all numbers n where the sum of the prime factors (with
multiplicity) of n is k. F is the Fibonacci sequence where F_1=1, F_2=1. Find
the last nine digits of the sum of S(F_i) for i = 2 to 24 '''

from pyprimesieve import primes as primes_to

def main():
    ''' Takes about a minute to finish '''
    fib = [1, 1]
    for _ in range(23):
        fib += [fib[-1] + fib[-2]]
    S = all_S_to(fib[23])
    print(sum(S[f] for f in fib[2:24]) % 10**9)

def all_S_to(n):
    ''' Returns a list S such that S[x] equals S(x) (mod 10**9) in the above
    definition of S for all x <= n '''
    primes = primes_to(n)
    S = [0 for _ in range(n+1)]
    S[0] = 1
    mod = 10**9
    # Dynamic programming solution based on finding the number of solutions to
    # a linear equation given the coefficients of the variables. Primes are
    # coefficients, the value of a variable in a given solution is the exponent
    # of its prime coefficient in the prime factorization of the number encoded
    # by the solution
    for p in primes:
        for i in range(p, n+1):
            # If p*S[i-p] were changed to just S[i-p], this would count the
            # number of solutions to the linear equation
            S[i] = (S[i] + p*S[i-p]) % mod
    return S

if __name__ == "__main__":
    main()
