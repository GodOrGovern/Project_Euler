''' Let φ be Euler's totient function. By iterating φ, each positive integer
generates a decreasing chain of numbers ending in 1. What is the sum of all
primes less than 40000000 which generate a chain of length 25? '''

from flint import fmpz
from pyprimesieve import primes

def main():
    ''' Driver function '''
    end = 40000000
    chain_lengths = [0] * end
    total = 0
    for p in primes(end):
        if prime_chain_length(p, chain_lengths) == 25:
            total += p
    print(total)

def prime_chain_length(prime, chain_lengths):
    ''' Returns the length of the chain of numbers produced by iterating
    Euler's totient function starting with 'prime' and ending with 1. Some
    chain lengths are saved in 'chain_lengths' '''
    prev = prime
    cur = prime - 1
    chain = [prev]
    length = 2
    while cur != 1:
        if chain_lengths[cur]:
            length = len(chain) + chain_lengths[cur]
            break
        chain += [cur]
        prev = cur
        cur = fmpz.euler_phi(fmpz(prev))
        length += 1
    for i, n in enumerate(chain):
        chain_lengths[n] = length - i
    return length

if __name__ == "__main__":
    main()
