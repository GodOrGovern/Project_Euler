''' A number consisting entirely of ones is called a repunit. We shall define
R(k) to be a repunit of length k. Given that n is a positive integer and
GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which
R(k) is divisible by n, and let A(n) be the least such value of k. You are
given that for all primes, p > 5, that p − 1 is divisible by A(p). Find the
sum of the first twenty-five composite values of n for which GCD(n, 10) = 1 and
n − 1 is divisible by A(n). '''

from itertools import count
from pyprimesieve import primes

def main():
    ''' The solution must be > 1000000 as A(n) < n. This function iterates over
    valid values of 'n' (not prime and not divisible by 2 or 5) starting at 2
    until 25 solutions are found. The sum of these solutions is then printed '''
    found = []
    prime = set(primes(100000))
    for n in count(2):
        if n not in prime and n % 2 and n % 5 and (n-1) % brute_check(n) == 0:
            found += [n]
            if len(found) == 25:
                break
    print(sum(found))

def brute_check(n):
    ''' Finding 'k' given 'n' is equivalent to solving 10^k mod 9*n = 1. This
    function tests possible values of 'k' starting at 1 until a solution is
    found. It returns the solution, which is the lowest value of 'k' that
    satisfies the above equation '''
    cur = 10
    for k in count(1):
        if cur == 1:
            return k
        cur = cur*10 % (9*n)

if __name__ == "__main__":
    main()
