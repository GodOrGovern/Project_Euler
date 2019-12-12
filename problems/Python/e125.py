''' Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares '''

from itertools import combinations
from euler import get_palindromes

def main():
    ''' Driver function '''
    end = 10**8
    sqr_sums = square_sums(end)
    print(sum(sqr_sums.intersection(get_palindromes(1, end))))

def square_sums(end):
    ''' Returns a set of all possible sums of consecutive squares, which go
    up to 'end' '''
    sums = dict()
    sqrs = squares_to(end)
    stop = int(end**0.5)
    for a in range(1, stop):
        val = sqrs[a] + sqrs[a+1]
        if val >= end:
            break
        sums[(a, a+1)] = sqrs[a] + sqrs[a+1]
        for b in range(a+2, stop+1):
            val = sums[(a, b-1)] + sqrs[b]
            if val >= end:
                break
            sums[(a, b)] = val
    return {n for n in sums.values()}

def squares_to(end):
    ''' Returns a list of squares up to 'end'. The value at each index 'i' is
    'i**2 '''
    sqrs = [0]
    n = 1
    n_sqr = 1
    while n_sqr < end:
        sqrs.append(n_sqr)
        n_sqr += 2*n + 1
        n += 1
    if n_sqr == end:
        sqrs.append(n_sqr)
    return sqrs

if __name__ == "__main__":
    main()