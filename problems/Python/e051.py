''' Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family '''

from itertools import chain
from collections import Counter
from primesieve import primes as primes_to

def main():
    ''' Driver function '''
    primes = primes_to(10**6)
    fam, count = large_fam(primes)
    if count == 8:
        print(low_member(fam, primes))

def large_fam(primes):
    ''' Find the largest prime family in primes. Return the family and its size '''
    all_fams = []
    for p in primes:
        all_fams.append(prime_fams(p))
    all_fams = list(chain.from_iterable(all_fams))
    count = Counter(all_fams)
    return count.most_common(1)[0]

def prime_fams(num):
    ''' Generate prime families that num belongs to '''
    num = str(num)
    fams = ['x', num[0]]
    for n in num[1:-1]:
        cur_fams = []
        for f in fams:
            if 'x' in f:
                index = f.index('x')
                if num[index] == n:
                    cur_fams.append(f+'x')
            else:
                cur_fams.append(f+'x')
            cur_fams.append(f+n)
        fams = cur_fams
    if len(num) > 1:
        return [f+num[-1] for f in fams[:-1]]
    return fams[0]

def low_member(fam, primes):
    ''' Find the lowest member of a prime family '''
    num = 0
    digit = '0'
    while num not in primes:
        num = int(fam.replace('x', digit))
        digit = chr(ord(digit)+1)
    return num

if __name__ == "__main__":
    main()
