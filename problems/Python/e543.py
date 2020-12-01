''' Define function P(n,k) = 1 if n can be written as the sum of k prime
numbers (with repetitions allowed), and P(n,k) = 0 otherwise. Let S(n) be the
sum of all P(i,k) over 1 <= i,k <= n. Let F(k) be the kth Fibonacci number
(with F(0) = 0 and F(1) = 1). Find the sum of all S(F(k)) over 3 <= k <= 44 '''

from math import ceil
from pyprimesieve import primes

def main():
    ''' Driver function '''
    fib = [0, 1]
    for _ in range(43):
        fib += [fib[-1] + fib[-2]]
    print(sum(S(n) for n in fib[3:]))

def S(n):
    ''' Uses Goldbach's conjecture, which has been verified for integers in the
    range required by the problem. The sum of all P(m, 1) for 1 <= m <= n is
    the number of primes <= n. The sum of all P(m, 2) is the number of even
    integers in 4 <= m <= n plus the number of integers in 6 <= m <= n equal to
    a prime plus 2. The sum of all P(m, k) with k >= 3 is the sum of all
    integers in 6 <= m <= n floor divided by 2 minus 2 (subtract 2 for each m
    or subtract 2*(n-6) once). 'P_n_k' is a closed form expression that
    calculates this '''
    prime = primes(n+1)
    P_n_1 = len(prime)
    P_n_2 = 0 if n < 4 else (n//2)-1 + (prime[-1]+2 <= n) + P_n_1 - 2
    P_n_k = 0 if n < 6 else (ceil((7-n)/2)**2 - 7*ceil((7-n)/2) + (n//2)**2 + (n//2) - 4*n + 20) // 2
    return P_n_1 + P_n_2 + P_n_k
