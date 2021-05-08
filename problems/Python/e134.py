''' For every pair of consecutive primes, p2 > p1 and p1 >= 5, there exist
values of n for which the last digits are formed by p1 and n is divisible by
p2. Let S be the smallest of these values of n.  Find the sum of S for every
pair of consecutive primes with 5 <= p1 <= 10**6'''

from math import log
from pyprimesieve import primes_nth
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    print(sum_S_to(10**6))

def sum_S_to(n):
    ''' Returns the sum of values of S (as described in the problem) for all
    consecutive primes p1 and p2, p2 > p1 and 5 <= p1 <= n '''
    total = 0
    primes = primes_to(n)
    # Get p2 for last p1
    primes += [primes_nth(len(primes)+1)]
    # The lowest positive value of n that satisfies both n = 0 (mod p2) and
    # n = p1 (mod 10**k) (k being the number of digits in p1) is S for that
    # pair of primes. The function (easily derived from modular relations)
    #    n(x) = pow_10*(x*p2 - p1*pow_10_mult_inv) + p1
    # (pow_10 is 10**k and pow_10_mult_inv is the multiplicative inverse of
    # 10**k mod p2) produces all valid values of n for a given p1,p2 pair
    for p1, p2 in zip(primes[2:-1], primes[3:]):
        p1_digits = int(log(p1, 10)) + 1
        pow_10 = 10**p1_digits
        pow_10_mult_inv = pow(pow_10, -1, p2)
        # Find the lowest value of x for which n(x) is positive
        x = int((-p1/pow_10 + p1*pow_10_mult_inv)/p2)+1
        total += pow_10*(x*p2 - p1*pow_10_mult_inv) + p1
    return total

if __name__ == "__main__":
    main()
