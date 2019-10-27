''' 5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.  Let S(L) be the sum of the
numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming
number. Find S(10**12). Give your answer modulo 2**32. '''

from pyprimesieve import factorize
from flint import fmpz

def main():
    ''' Driver function '''
    end = 10**6
    total = 0
    for n in range(1, end+1):
        valid = True
        for p, e in factorize(n):
            if p not in {2, 3, 5} and (e != 1 or not smooth(p-1)):
                valid = False
                break
        if valid:
            total += n
    print(total)

def smooth(p):
    ''' Determine if 'p' is 5-smooth '''
    while not p % 5: p //= 5
    while not p % 3: p //= 3
    while not p % 2: p //= 2
    return p == 1

if __name__ == "__main__":
    main()
