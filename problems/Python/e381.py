''' For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5. Find ∑S(p) for 5 ≤
p < 10**8. '''

from pyprimesieve import primes as primes_to

# https://math.stackexchange.com/questions/200723/simplifying-p-1-p-2-p-3-p-4-p-5-bmod-p
def main():
    ''' Driver function '''
    total = 0
    mult = {1: 3, 3: 1, 5: 7, 7: 5}
    for p in primes_to(10**8)[2:]:
        total += (mult[p%8]*p - 3) // 8
    print(total)

if __name__ == "__main__":
    main()
