''' For every positive number n we define the function streak(n)=k as the
smallest positive integer k such that n+k is not divisible by k+1. Define
P(s,N) to be the number of integers n, 1<n<N, for which streak(n)=s. Find the
sum, as i ranges from 1 to 31, of P(i,4**i) '''

from pyprimesieve import factorize
from collections import defaultdict

def main():
    ''' Driver function '''
    total = 0
    min_num = [lcm(n) for n in range(1, 33)]
    for i, n in enumerate(min_num[:-1]):
        if min_num[i+1] == n:
            continue
        total += multiples(n, min_num[i+1], 4**(i+1))
    print(total-1)

def lcm(num):
    ''' Find the smallest positive number that is divisible by all the numbers
    from 1 to 'num' '''
    factor = defaultdict(int)
    for n in range(1, num+1):
        for p, e in factorize(n):
            factor[p] = max(factor[p], e)
    total = 1
    for p, e in factor.items():
        total *= p**e
    return total

def multiples(factor, not_factor, end):
    ''' Find all numbers below 'end' that are multiples of 'factor' but are
    not divisible by 'not_factor' '''
    count = 0
    for n in range(factor, end, factor):
        count += n % not_factor != 0
    return count

if __name__ == "__main__":
    main()
