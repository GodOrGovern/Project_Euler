''' Find the number of integers 1 < n < 10**7, for which n and n + 1 have the
same number of positive divisors '''

from pyprimesieve import primes, factorize

def main():
    ''' Driver function '''
    total = 0
    num_divs = find_num_divisors(10**7)
    for i, n in enumerate(num_divs[:-1]):
        total += n == num_divs[i+1]
    print(total)

def find_num_divisors(end):
    ''' Calculate the number of divisors for each number up to 'end' '''
    num_divisors = [0 for _ in range(2, end)]
    prime = set(primes(10**7))
    for n in range(2, end):
        divisors = 1
        if n not in prime:
            factors = factorize(n)
            for _, e in factors:
                divisors *= (e + 1)
        num_divisors[n-2] = divisors
    return num_divisors

if __name__ == "__main__":
    main()
