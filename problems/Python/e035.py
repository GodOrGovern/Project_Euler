''' How many circular primes are there below one million? '''

from sympy.ntheory import isprime
from pyprimesieve import primes

def main():
    ''' Find number of circular primes below 1,000,000 '''
    count = 0
    nums = set(primes(1000000))
    while nums:
        num = str(nums.pop())
        perms = {int(num[i:]+num[:i]) for i in range(len(num))}
        if {isprime(p) for p in perms} == {True}:
            count += len(perms)
        nums.difference_update(perms)
    print(count)

if __name__ == "__main__":
    main()
