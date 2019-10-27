''' Find the smallest number with 2**500500 divisors. Give your answer modulo
500500507 '''

from pyprimesieve import primes

def main():
    ''' Driver function '''
    vals = get_vals(10**7)
    total = 1
    mod = 500500507
    for v in vals[:500500]:
        total = total*(v % mod) % mod
    print(total)

def get_vals(end):
    ''' This post explains it: https://bit.ly/2J9ByKf '''
    vals = primes(end)
    n = 0
    while vals[n] < end**0.5:
        val, l = 0, 1
        while val < end:
            val = vals[n]**2**l
            vals.append(val)
            l += 1
        n += 1
    return sorted(vals)

if __name__ == "__main__":
    main()
