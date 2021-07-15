''' We shall say that M(n, d) represents the maximum number of repeated digits
for an n-digit prime where d is the repeated digit and S(n, d) represents the
sum of these primes. Find the sum of all S(10, d) for 1 <= d <= 9 '''

from itertools import combinations_with_replacement
from sympy.utilities.iterables import multiset_permutations
from sympy import isprime

def main():
    ''' Driver function '''
    print(S(10))

def S(num_digits):
    ''' Returns the sum of the S(n, d) function described in the problem across
    all values of d (1 through 9) given that n = num_digits '''
    num_subs = 1
    prime_sum = 0
    cur_ds = set(range(10))
    while cur_ds:
        next_ds = set(cur_ds)
        for d in cur_ds:
            d_repeated = (d,) * (num_digits - num_subs)
            for subs in combinations_with_replacement(range(10), num_subs):
                for perm in multiset_permutations(d_repeated + subs, num_digits):
                    if perm[0] == 0:
                        continue
                    num = int(''.join(map(str, perm)))
                    if isprime(num):
                        prime_sum += num
                        next_ds -= {d}
        num_subs += 1
        cur_ds = next_ds
    return prime_sum

if __name__ == "__main__":
    main()
