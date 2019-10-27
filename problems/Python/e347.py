''' For two distinct primes p and q let M(p,q,N) be the largest positive
integer ≤ N only divisible by both p and q and M(p,q,N)=0 if such a positive
integer does not exist. Let S(N) be the sum of all distinct M(p,q,N). Find
S(10,000,000). '''

from math import log
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    end = 10**7
    primes = primes_to(end // 2)
    total = 0
    for i, p1 in enumerate(primes):
        if p1**2 > end:
            break
        for p2 in primes[i+1:]:
            if p1 * p2 > end:
                break
            total += M(p1, p2, end)
    print(total)

def M(p1, p2, end):
    ''' Returns the largest natural number divisible by both 'p1' and 'p2' that is
    below 'end'. Assumes 'p1' is less than 'p2'. Returns 0 if p1*p2 > end '''
    if p1 * p2 > end:
        return 0
    n = p1**int(log(end/p2, p1))
    cur_max = 0
    while n != 1:
        cur = n * p2**int(log(end/n, p2))
        cur_max = max(cur, cur_max)
        n //= p1
    return cur_max

if __name__ == "__main__":
    main()
