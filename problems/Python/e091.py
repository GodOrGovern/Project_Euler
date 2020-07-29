''' The points P = (x1, y1) and Q = (x2, y2) are plotted at integer co-ordinates
and are joined to the origin to form ΔOPQ. Given that 0 ≤ x1, y1, x2,
y2 ≤ 50, how many right triangles can be formed? '''

from math import gcd

def main():
    ''' The number of triangles with the hypotenuse between points P and Q is
    just the range of values (50 in this case) squared. All other triangles can
    be found by iterating over all possible values for one coordinate (a, b) and then
    using the Extended Euclidean Algorithm to find solutions to the equation
    ax+by=c where c=a**2+b**2. Once one (x, y) pair has been found for a given
    (a, b) all others can be generated. A set is used to keep track of valid
    points to avoid duplicates '''
    end = 2
    solutions = set()
    for a in range(end+1):
        for b in range(1 if a == 0 else a, end+1):
            c = a**2 + b**2
            div = gcd(a, b)
            if c % div != 0:
                continue
            mult = c // div
            x, y = ext_euclid(a, b)
            x, y = mult*x, mult*y
            for n in range((x-end)*div//b, x*div//b + 1):
                x1 = x - n * (b // div)
                y1 = y + n * (a // div)
                if 0 <= x1 <= end and 0 <= y1 <= end and (a, b) != (x1, y1):
                    solutions.add(tuple(sorted([(a, b), (x1, y1)])))
                    solutions.add(tuple(sorted([(b, a), (y1, x1)])))
    print(len(solutions) + end**2)

def ext_euclid(a, b):
    ''' Returns solutions for x and y in the equation ax + by = gcd(a, b) '''
    q = 0
    r0, r1, rNext = a, b, a
    s0, s1, sNext = 1, 0, 1
    t0, t1, tNext = 0, 1, 0
    while r1 != 0:
        q = r0 // r1
        rNext = r0 - r1*q
        sNext = s0 - s1*q
        tNext = t0 - t1*q
        r0, r1 = r1, rNext
        s0, s1 = s1, sNext
        t0, t1 = t1, tNext
    return s0, t0

if __name__ == "__main__":
    main()
