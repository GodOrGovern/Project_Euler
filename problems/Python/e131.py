''' There are some prime values, p, for which there exists a positive integer,
n, such that the expression n^3 + (n^2)*p is a perfect cube.  What is perhaps most
surprising is that for each prime with this property the value of n is unique,
and there are only four such primes below one-hundred.  How many primes below
one million have this remarkable property? '''

from pyprimesieve import primes

def main():
    ''' 'n' must be a cube. This function iterates over all cubes up to 600^3
    for each prime. 'found' keeps track of the number of valid '(n, p)' pairs.
    This amount is printed at the end. This solution is relatively slow (about
    30 seconds) '''
    found = 0
    cubes = [n**3 for n in range(1, 600)]
    for p in primes(1000000):
        for n in cubes:
            cur = n*n*(n+p)
            if round(cur**(1/3))**3 == cur:
                found += 1
                break
    print(found)

if __name__ == "__main__":
    main()
