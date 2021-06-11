''' For a positive integer n, let f(n) be the sum of the squares of the digits
(in base 10) of n. Find the last nine digits of the sum of all n, 0 < n <
10**20, such that f(n) is a perfect square. '''

from math import factorial
from functools import reduce
from operator import mul

def main():
    ''' Driver function '''
    print(sum_f_n(20) % 10**9)

def sum_permutations(digits):
    ''' Given a list 'digits' containing 1 or more single digit numbers (ie
    0-9), returns the sum of all unique numbers that can be formed using each
    of the numbers in 'digits' exactly once. Leading zeroes are allowed and the
    same value can appear more than once in 'digits' '''
    n = len(digits)
    digit_counts = [digits.count(i) for i in range(10)]
    num_perms = factorial(n) // reduce(mul, map(factorial, digit_counts), 1)
    sum_pows_10 = sum(10**i for i in range(n))
    total = 0
    for digit in range(10):
        # the number of times 'digit' appears in each index or place value
        # across all permutations
        digit_freq = num_perms * digit_counts[digit] // n
        total += digit * digit_freq * sum_pows_10
    return total

def sum_f_n(max_digits):
    ''' Returns the sum of all numbers n (with the number of digits in n <=
    'max_digits' and n > 0) such that f(n) is perfect square, where f(n) is the
    sum of the squares of the digits of n (in base 10). '''
    digits = 20
    sqrs = {n*n for n in range(int(9*max_digits**0.5)+1)}
    sqr_digits = [n*n for n in range(10)]
    # stores 2-tuples, each of which contains a unique ordered tuple of digits
    # (n) and the sum of the squares of those digits (f_n)
    cur_nums = [(n*n, (n,)) for n in range(1, 10)]
    total = sum(45*10**i for i in range(digits))
    for cur_digits in range(1, max_digits):
        next_nums = []
        for (f_n, n) in cur_nums:
            # only iterate over digits that are <= the first digit in n to
            # prevent overlapping. 0 is skipped because it doesn't affect f_n
            # and can be accounted for later
            for i, s in enumerate(sqr_digits[1:n[0]+1]):
                new_f_n, new_n = f_n+s, (i+1,)+n
                if new_f_n in sqrs:
                    # n doesn't need to contain zeroes because f_n is the same
                    # regardless. The function sum_permutations allows leading
                    # zeroes, meaning such values have to be subtracted out.
                    # Instead of finding sum_permutations for n + x zeroes and
                    # then subtracting sum_permutations for n + (x-1) zeroes
                    # across all possible values of x, one can simply do
                    # sum_permutations for x + the maximum number of 0s
                    # possible, which accounts for all of them.
                    total += sum_permutations(new_n+(0,)*(max_digits-cur_digits-1))
                next_nums.append((new_f_n, new_n))
        cur_nums = next_nums
    return total

if __name__ == "__main__":
    main()
