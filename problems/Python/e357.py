''' Find the sum of all positive integers n not exceeding 100,000,000
such that for every divisor d of n, d+n/d is prime '''

from functools import reduce
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    total = 3
    end = int(1e8)
    primes = set(primes_to(end))
    total += check_lines(6, end, 36, primes)
    total += check_lines(30, end, 36, primes)
    total += check_lines(10, end, 12, primes)
    print(total)

def check_lines(start, end, step, primes):
    ''' Check all numbers up to 'end' on the line that has 'step' as slope and
    'start' as y-intercept. Return the sum of all numbers that have divisors
    which add to primes '''
    total = 0
    for n in range(start, end+1, step):
        if n+1 not in primes:
            continue
        if check_divs(n, primes):
            total += n
    return total

def check_divs(n, primes):
    ''' Check if divisor pairs of 'n' add to prime numbers '''
    for d1, d2 in divisors(n):
        if d1+d2 not in primes:
            return False
    return True

def divisors(n):
    ''' Generator for pairs of divisors of 'n' '''
    yield 1, n
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            yield i, n//i

if __name__ == "__main__":
    main()
