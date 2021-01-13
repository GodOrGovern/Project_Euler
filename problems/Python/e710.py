''' We shall define a twopal to be a palindromic tuple having at least one
element with a value of 2. It should also be noted that elements are not
restricted to single digits. Let t(n) be the number of twopals whose elements
sum to n. Find the least value of n such that t(n) is divisible by one
million '''

def main():
    ''' 't_n' = t(n) mod 10^6. At most, 3 consecutive values of the g function
    described in the above link need to be stored at any given time. These
    values are stored in 'g' in ascending order. Values of t(n) are generated
    until a value divisible by one million is found. 'n' is then printed.

    My equation (technically two, one for each parity) for t(n) uses the
    recursive function g described here, with k=2 (unrelated to below k):
        https://math.stackexchange.com/a/2086747/530956
    For even n:
        t(n) = g((n-2)/2) + (sum 2^((n-2m-2)/2)-g((n-2m)/2) for m=0 to n/2)
    For odd n:
        t(n) = sum 2^((n-2m-3)/2)-g((n-2m-1)/2) for m=0 to (n-1)/2
    A given k-length twopal, p, can be equivalently expressed using its first
    floor(k/2) elements (call them h) and middle element, m (0 if k is even).
    The sum of h, s = (n-m)/2. The problem is thus equal to the sum of the
    number of compositions of s containing 2 for all possible values of s.  The
    g recurrence relation described in the above link outputs the number of
    compositions that don't contain a 2, which one can subtract from 2^(x-1),
    the number of compositions of x, to get the correct value. When m=2 (only
    possible for even n as m = n (mod 2)) all compositions make valid twopals.
    The summation doesn't take this into account, so g((n-2)/2) needs to be
    added. The relationship between successive values of t(n) used below can
    easily be derived from the above equation(s) '''
    n = 6
    mod = 10**6
    t_n = 4
    g = [1, 2, 4]
    while t_n != 0:
        n += 1
        if n % 2 == 1:
            t_n -= g[0]
        else:
            t_n = (t_n + g[1] - g[2] + pow(2, (n-2)//2, mod)) % mod
            g = [g[1], g[2], (2*g[2]-g[1]+g[0]) % mod]
    print(n)

if __name__ == "__main__":
    main()
