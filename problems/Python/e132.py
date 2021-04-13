''' A number consisting entirely of ones is called a repunit. We shall define
R(k) to be a repunit of length k. Find the sum of the first forty prime
factors of R(10**9) '''

from pyprimesieve import primes

def main():
    ''' R(k) is equal to (10**k-1)/9. Thus, a number n divides R(k) IFF
    (10**k-1)/9 = 0 (mod n). This can be re-arranged to 10**k = 1 (mod 9*n),
    which allows for the use of modular exponentiation '''
    factors = []
    for n in primes(10**6):
        if pow(10, 10**9, 9*n) == 1:
            factors += [n]
        if len(factors) == 40:
            break
    print(sum(factors))

if __name__ == "__main__":
    main()
