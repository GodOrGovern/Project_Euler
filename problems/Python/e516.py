''' 5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers. Let S(L) be the sum of the
numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming
number. Find S(10**12). Give your answer modulo 2**32. '''

from sympy import isprime

def main():
    ''' Driver function '''
    print(S(10**12) % 2**32)

def S(n):
    ''' S(n) function described above. Derived primarily from the totient
    function definition totient(n) = n times the product series ((p-1)/p) for
    all distinct prime factors of n. Based on this, one can determine that in
    order for totient(n) to be hamming, n must not have a prime factor > 5
    raised to an exponent > 1 (any exponent is allowed for 2, 3, 5) and each of
    n's prime factors minus 1 must be a hamming number '''
    total = 0
    mod = 2**32
    hamming = gen_hamming(n)
    # List of primes one greater than a hamming number
    # No need for first three values [2, 3, 5]
    valid_primes = [x+1 for x in hamming if isprime(x+1)][3:]
    valid_prime_combs = all_prod_combs(valid_primes, n)
    for p in valid_prime_combs:
        if p*hamming[0] > n:
            break
        for m in hamming:
            val = p*m
            if val > n:
                break
            total += val
    return total + sum(hamming)

def all_prod_combs(ints, end):
    ''' Returns a sorted list of all possible products (below end) obtained
    from multiplying elements in ints without repeating elements. '''
    def helper(num, bases):
        ''' Returns a list of all possible products (below end) using num
        exactly once and each number in bases either zero or once '''
        prods = []
        recurse = True
        for i, b in enumerate(bases):
            val = num*b
            if val > end:
                break
            prods += [val]
            if val*ints[0] <= end:
                prods += helper(val, bases[i+1:])
        return prods
    return sorted(helper(1, ints))

def gen_hamming(end):
    ''' Returns a sorted list of all hamming numbers up to and including 'end' '''
    hamming = {1}
    prev = {1}
    while 2*min(prev) <= end:
        cur = set()
        for n in prev:
            cur.update({n*p for p in [2,3,5] if n*p <= end})
        hamming.update(cur)
        prev = cur
    return sorted(hamming)

if __name__ == "__main__":
    main()
