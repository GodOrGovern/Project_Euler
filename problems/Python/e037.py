''' Find the sum of the only eleven primes that are both truncatable from left
to right and right to left '''

from math import log10
from sympy import isprime, nextprime

def main():
    ''' Find sum of truncatable primes '''
    count, total = 0, 0
    prime = 11
    while count < 11:
        if {isprime(p) for p in truncate(prime)} == {True}:
            total += prime
            count += 1
        prime = nextprime(prime)
    print(total)

def truncate(num):
    ''' Generator that truncates number from both sides '''
    power = int(log10(num))
    for n in range(1, power + 1):
        yield num // (10**n)
    for n in range(power, 0, -1):
        yield num % (10**n)

if __name__ == "__main__":
    main()
