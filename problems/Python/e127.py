''' The radical of n, rad(n), is the product of distinct prime factors of n.
We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
    1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    2. a < b
    3. a + b = c
    4. rad(abc) < c
Find ∑c for c < 120000. '''

from functools import reduce
from operator import mul
from pyprimesieve import factorize

def main():
    ''' Driver function '''
    print(find_triplets_below(120000))

def find_triplets_below(end):
    ''' Returns the sum of c for valid triplets a,b,c with c < end as described
    in the problem prompt '''
    factors = [set(), {1}] + [set(p for p,e in factorize(n)) for n in range(2, end)]
    rad = [reduce(mul, f, 1) for f in factors]
    n_by_rad = sorted(range(end), key=lambda n: rad[n])
    def binary_search(target):
        ''' Returns the index i of n_by_rad such that rad[n_by_rad[i]] is as
        close to target as possible '''
        low, high = 0, end-1
        while low <= high:
            mid = (low + high) // 2
            if rad[n_by_rad[mid]] == target:
                return mid
            if rad[n_by_rad[mid]] < target:
                low = mid+1
            else:
                high = mid-1
        return high
    total = 0
    for c in range(3, end):
        for n in n_by_rad[:binary_search(c // rad[c])]:
            # Avoids negative values and duplicates
            if n > c or c-n < n:
                continue
            a, b = n, c-n
            if (factors[a] & factors[b]) or (factors[a] & factors[c]) or (factors[b] & factors[c]):
                continue
            if rad[a]*rad[b]*rad[c] < c:
                total += c
    return total

if __name__ == "__main__":
    main()
