''' Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum '''

from primesieve import primes as primes_to

def main():
    ''' The value n/φ(n) will be minimized when n is the product of two large
    primes. This performs a bruteforce check for possible pairs of primes and
    keeps track of the minimum '''
    primes = primes_to(10000)
    cur_min = [2, 0]
    for i, p1 in enumerate(primes[::-1]):
        for p2 in primes[::-1][i+1:]:
            n = p1*p2
            phi = (p1-1)*(p2-1)
            if sorted(str(n)) == sorted(str(phi)):
                if n < 10**7 and n/phi < cur_min[0]:
                    cur_min = [n/phi, n]
    print(cur_min[1])

if __name__ == "__main__":
    main()
