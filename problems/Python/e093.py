''' By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, −, *, /) and
brackets/parentheses, it is possible to form different positive integer
targets. Note that concatenations of the digits are not allowed. Find the set
of four distinct digits, a < b < c < d, for which the longest set of
consecutive positive integers, 1 to n, can be obtained, giving your answer as
a string: abcd '''

from operator import mul, add, sub
from collections import defaultdict
from itertools import combinations, permutations, product, count

def main():
    ''' Driver function '''
    found = defaultdict(set)
    for nums in combinations((n for n in range(10)), 4):
        found[nums].update(expressions(nums))
    print(int(''.join(str(n) for n in consecutive(found))))

def expressions(nums):
    ''' Returns a set that includes all natural numbers that can be reached
    using the elements of 'nums' and the four basic arithmetic
    operations. Assumes 'nums' only has four elements '''
    found = set()
    for a, b, c, d in permutations(nums):
        for f, g, h in product([add, sub, mul, div], repeat=3):
            try:
                vals = [f(g(h(a, b), c), d),
                        f(h(a, g(b, c)), d),
                        g(h(a, b), f(c, d)),
                        h(a, f(g(b, c), d)),
                        h(a, f(b, g(c, d)))]
                for v in vals:
                    if int(v) == v and v > 0:
                        found.add(int(v))
            except ZeroDivisionError:
                continue
    return found

def consecutive(found):
    ''' For each entry in the dict 'found', checks how many consecutive
    numbers (starting at 1) appear in the corresponding set. Returns the key with the most consecutive numbers '''
    maximum = 0
    max_key = None
    for key, val in found.items():
        for n in count(1):
            if n not in val:
                if n-1 > maximum:
                    maximum = n-1 
                    max_key = key
                break
    return max_key

def div(a, b):
    ''' Same as a / b '''
    return a / b

if __name__ == "__main__":
    main()