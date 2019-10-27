''' What is the first value which can be written as the sum of primes in over
five thousand different ways? '''

from primesieve import primes as primes_to
from euler import partition

def main():
    ''' Driver function '''
    primes = primes_to(100)
    total, num = 0, 0
    while total < 5000:
        num += 1
        total = partition(primes, num)
    print(num)

if __name__ == "__main__":
    main()
