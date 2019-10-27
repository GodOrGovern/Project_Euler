''' Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k '''

from math import log10
from mpmath import fibonacci

def main():
    ''' Driver function '''
    count = 2
    vals = {str(n) for n in range(1, 10)}
    p, pp = 1, 1
    cur = 2
    while set(str(cur)) != vals or not check_first(count, vals):
        cur = (p + pp) % 10**9
        pp = p
        p = cur
        count += 1
    print(count)

def check_first(n, vals):
    ''' Checks if the first ten digits of the 'nth' Fibonacci number are
    equal to the set 'vals' '''
    num = int(fibonacci(n))
    digits = int(log10(num)) + 1
    return vals == set(str(num // 10**(digits - 9)))

if __name__ == "__main__":
    main()
