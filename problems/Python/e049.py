''' The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this
sequence? '''

from itertools import permutations
from primesieve.numpy import primes as primes_to

def main():
    ''' Driver function '''
    perms = prime_perms()
    diff, base = check_diff(perms)
    result = str(base-diff) + str(base) + str(base+diff)
    print(result)

def prime_perms():
    ''' Find all primes that are permutations of each other '''
    primes = primes_to(10000)
    primes = set(primes[primes > 1000])
    valid = []
    while primes:
        prime = primes.pop()
        perms = set(num_perms(prime))
        perms.intersection_update(primes)
        perms.add(prime)
        if len(perms) >= 3:
            valid.append(list(perms))
        primes.difference_update(perms)
    return valid

def num_perms(num):
    ''' Return all permutations of num '''
    num = list(str(num))
    perms = []
    for p in permutations(num):
        perms.append(int(''.join(p)))
    return perms

def check_diff(perms):
    ''' Check differences between prime permutations. When a prime and its
    permutations have at least one difference in common, return the
    difference, and current prime '''
    for p in perms:
        p.sort()
        for cur in p:
            diffs = []
            for n in p:
                diff = abs(cur-n)
                if diff in diffs:
                    return diff, cur
                diffs.append(diff)
    return None

if __name__ == "__main__":
    main()
