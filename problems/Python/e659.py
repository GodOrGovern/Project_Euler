''' Let P(k) be the largest prime that divides any two successive terms of the
sequence n**2+k**2. Find the last 18 digits of ∑P(k) for k=1 to 10**9 '''

from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    end = 10**5
    primes = primes_to(2*end + 1)
    points = point_primes(end, primes)
    vals = [[n**2 + 1, 1] for n in range(end)]
    for n in range(10**2):
        result = find_point(vals, points, n)
        if not result:
            print(n)

def find_point(vals, points, cur):
    ''' Find the prime that divides successive terms of the function x**2 +
    'cur**2' and return it if found. If not found, return None '''
    n = 0
    while n < len(vals):
        if vals[n][1] < cur:
            old = vals[n][1]
            vals[n][0] += (cur-old) * (cur+old)
            vals[n][1] = cur
        for p in points[n]:
            if not vals[n][0] % p:
                return p
        n += 1
    return None


def point_primes(end, primes):
    ''' Find primes that could divide successive terms starting at 'n' for each
    point in the range '1..end' and store them in 'points'. Returns the list of
    sets of primes ('points') '''
    points = [set() for n in range(end)]
    for n in range(1, end):
        val = 2*n + 1
        for p in primes:
            if p > val:
                break
            if not val % p:
                points[n].add(p)
    return points

if __name__ == "__main__":
    main()
