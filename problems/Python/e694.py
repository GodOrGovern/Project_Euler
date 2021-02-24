''' A positive integer n is considered cube-full, if for every prime p that
divides n, so does p**3. Let s(n) be the function that counts the number of
cube-full divisors of Let S(n) represent the summatory function of s, that is
S(n) = sum of s(i) for i = 1 to n. Find S(10**18) '''

from operator import mul
from bisect import bisect
from functools import reduce
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    print(S(1e18))

def S(n):
    ''' Equivalent to the S(n) function described above '''
    return sum(int(n)//x for x in get_cube_fill(n)) + int(n)

def get_cube_fill(end):
    ''' Returns the set of all cube-filled numbers up to 'end' excluding 1 '''
    all_cube = set()
    for base in get_cube_fill_bases(end):
        base_int = reduce(mul, base, 1)**3
        all_cube.add(base_int)
        cur_cube = {base_int}
        while cur_cube:
            new_cube = set()
            for cur in cur_cube:
                for prime in base:
                    new = cur * prime
                    while new <= end:
                        new_cube.add(new)
                        new *= prime
            cur_cube = new_cube
            all_cube |= new_cube
    return all_cube

def get_cube_fill_bases(end):
    ''' Returns the set of all possible prime factorizations (disregarding
    exponents) for cube-filled numbers up to 'end' '''
    primes = primes_to(int(end**(1/3)) + 1)
    all_bases = cur_bases = {(p,) for p in primes}
    while any(cur_bases):
        new_bases = set()
        for factors in cur_bases:
            start = bisect(primes, factors[-1])
            highest_val = int(end**(1/3) / reduce(mul, factors, 1))
            stop = bisect(primes, highest_val)
            new_bases |= {factors+(p,) for p in primes[start:stop]}
        cur_bases = new_bases
        all_bases |= new_bases
    return all_bases

if __name__ == "__main__":
    main()
