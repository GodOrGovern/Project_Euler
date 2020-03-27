''' Let N be a positive integer and let N be split into k equal parts, r = N/k,
so that N = r + r + ... + r.  Let P be the product of these parts, P = r × r ×
... × r = r**k.  Let M(N) = P_max for a given value of N. Let D(N) = N if M(N)
is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.
Find ∑ D(N) for 5 ≤ N ≤ 10000 '''

from mpmath import mpf
from math import gcd
from pyprimesieve import factorize

def main():
    ''' Driver function '''
    total = 0
    for n in range(5, 10001):
        denom = m(n)
        terminate = True
        for p, _ in factorize(denom // gcd(n, denom)):
            if p not in {2, 5}:
                terminate = False
                break
        total += n if not terminate else -n
    print(total)

def m(n):
    ''' Find P_max given n '''
    def search(l, r, last):
        ''' Find the peak '''
        mid = (l + r) // 2
        left = (mpf(n) / (mid-1))**(mid-1)
        cur = (mpf(n) / mid)**mid
        right = (mpf(n) / (mid+1))**(mid+1)
        if cur > left and cur > right:
            return mid
        if cur > left and cur < right:
            return search(mid+1, r, mid)
        if cur < left and cur > right:
            return search(l, mid-1, mid)
    return search(2, n-1, 1)

if __name__ == "__main__":
    main()
