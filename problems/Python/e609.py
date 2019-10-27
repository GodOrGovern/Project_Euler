''' For every n ≥ 1 the prime-counting function π(n) is equal to the number of
primes not exceeding n. We say that a sequence of integers u=(u0,⋯,u_m) is a π
sequence if u_n ≥ 1 for every n; u_n + 1 = π(u_n); u has two or more elements
Let c(u) be the number of elements of u that are not prime.  Let p(n,k) be the
number of π sequences u for which u_0 ≤ n and c(u)=k. Let P(n) be the product
of all p(n,k) that are larger than 0. Find P(10**8). Give your answer modulo
1000000007 '''

from collections import defaultdict
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    end = 10**1
    mod = 10**9 + 7
    primes = primes_to(end)
    pi = prime_count(primes, end)
    values = k_values(pi, set(primes), end)
    print(product(values, mod))

def prime_count(primes, end):
    ''' Return value of π(n) for all n below and equal to 'end' '''
    pi = [0] * (end+1)
    for i, p in enumerate(primes[:-1]):
        pi[p:primes[i+1]+1] = [pi[p-1] + 1] * (primes[i+1]-p+1)
    pi[primes[-1]:end+1] = [pi[primes[-1]-1] + 1] * (end-primes[-1]+1)
    return pi

def k_values(pi, primes, end):
    ''' Find the the number of pi sequences with k non-prime numbers
    for all possible values of k. A list with the indexes as k and the values
    as the number of pi sequences is returned '''
    values = [0] * longest_seq(pi, end)
    for n in range(2, end+1):
        cur = n
        not_prime = cur not in primes
        while cur != 1:
            cur = pi[cur]
            not_prime += cur not in primes
            values[not_prime] += 1
    return values

def longest_seq(pi, end):
    ''' Get length of longest possible pi sequence given high starting value of
    'end' '''
    cur = end
    length = 1
    while cur != 1:
        cur = pi[cur]
        length += 1
    return length

def product(arr, mod):
    ''' Return the product of all non-zero values in 'arr' modulo 'mod' '''
    result = 1
    for n in arr:
        if n > 1:
            result = result * n % mod
    return result

if __name__ == "__main__":
    main()
