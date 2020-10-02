''' A number consisting entirely of ones is called a repunit. We shall define
R(k) to be a repunit of length k. Given that n is a positive integer and
GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which
R(k) is divisible by n, and let A(n) be the least such value of k; for example.
Find the least value of n for which A(n) first exceeds one-million. '''

from itertools import count

def main():
    ''' The solution must be > 1000000 as A(n) < n. This function iterates over
    valid values of 'n' (not divisible by 2 or 5) starting at 1000000 until a
    solution is found '''
    for n in count(1000000):
        if n % 2 and n % 5 and brute_check(n) > 1000000:
            print(n)
            break

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
