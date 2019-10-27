''' A riffle shuffle is executed as follows: a deck of cards is split into two
equal halves, with the top half taken in the left hand and the bottom half
taken in the right hand. Next, the cards are interleaved exactly, with the top
card in the right half inserted just after the top card in the left half, the
2nd card in the right half just after the 2nd card in the left half, etc.
Let s(n) be the minimum number of consecutive riffle shuffles needed to restore
a deck of size n to its original configuration, where n is a positive even
number. Find the sum of all values of n that satisfy s(n)=60 '''

from functools import reduce
from pyprimesieve import factorize

# https://math.stackexchange.com/questions/753712/modulo-arithmetic-a-1-mod-n
def main():
    ''' Driver function '''
    shuffles = 60
    end = 2**shuffles
    count = 0
    for n in gen_divisors(end-1):
        val = (end - 1) // n
        if multi_order(2, val) == shuffles:
            count += val + 1
    print(count)

# https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def gen_divisors(n):
    ''' Generator for divisors of 'n' '''
    factors = factorize(n)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def multi_order(a, n):
    ''' Return the multiplicative order of 'a**k % n == 1'. Assumes 'gcd(a, n)'
    is 1. The function returns -1 if 'k' exceeds 'n' '''
    result, k = 1, 1
    while k < n:
        result = result * a % n
        if result == 1:
            return k
        k += 1
    return -1

if __name__ == "__main__":
    main()
