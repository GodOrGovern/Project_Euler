''' 5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers. Let S(L) be the sum of the
numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming
number. Find S(10**12). Give your answer modulo 2**32. '''

from sympy import isprime

def main():
    ''' Driver function '''
    end = 10**12
    hamming = gen_hamming(end)
    primes = prime_minus_one(hamming)
    print(primes)
    print(len(primes))

def prime_minus_one(nums):
    ''' Return all primes that are 1 above any number in 'nums' '''
    primes = set()
    for n in nums:
        if isprime(n+1):
            primes.add(n+1)
    return primes

def gen_hamming(end):
    ''' Generate all hamming numbers up to 'end' '''
    smooth = {1}
    min_cur = 1
    prev = {1}
    while min_cur*2 < end:
        min_cur = float("inf")
        cur = set()
        for n in prev:
            for s in [2,3,5]:
                temp = n*s
                if temp <= end:
                    cur.add(temp) 
                    min_cur = min(min_cur, temp)
        smooth.update(cur)
        prev = cur
    return smooth

if __name__ == "__main__":
    main()