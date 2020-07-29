''' The points P = (x1, y1) and Q = (x2, y2) are plotted at integer co-ordinates
and are joined to the origin to form ΔOPQ. Given that 0 ≤ x1, y1, x2,
y2 ≤ 50, how many right triangles can be formed? '''

#from math import gcd

def main():
    ''' The number of triangles with the hypotenuse between points P and Q is
    just the range of values (50 in this case) squared. All other triangles can
    be found by iterating over all possible values for one coordinate (a, b) and then
    using the Extended Euclidean Algorithm to find solutions to the equation
    ax+by=c where c=a**2+b**2. Once one (x, y) pair has been found for a given
    (a, b) all others can be generated. A set is used to keep track of valid
    points to avoid duplicates '''
    end = 50
    solutions = set()
    for a in range(end+1):
        for b in range(1 if a == 0 else a, end+1):
            gcd, x, y = xgcd(a, b)
            mult = (a**2 + b**2) // gcd
            x, y = x*mult, y*mult
            for n in range((x-end)*gcd//b, x*gcd//b + 1):
                x1, y1 = x - n * (b // gcd), y + n * (a // gcd)
                if 0 <= x1 <= end and 0 <= y1 <= end and (a, b) != (x1, y1):
                    solutions.add(tuple(sorted([(a, b), (x1, y1)])))
                    solutions.add(tuple(sorted([(b, a), (y1, x1)])))
    print(len(solutions) + end**2)

def xgcd(a, b):
    ''' Returns gcd(a, b) and solutions for x and y in the equation ax + by = gcd(a, b) '''
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        x0, x1 = x1, x0 - x1*q
        y0, y1 = y1, y0 - y1*q
    return b, x0, y0

if __name__ == "__main__":
    main()
