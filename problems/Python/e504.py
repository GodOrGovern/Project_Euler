''' Let ABCD be a quadrilateral whose vertices are lattice points lying on the
coordinate axes as follows: A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a,
b, c, d ≤ m and a, b, c, d, m are integers.  How many quadrilaterals ABCD
strictly contain a square number of lattice points for m = 100? '''

from math import gcd
from itertools import product

def main():
    ''' Driver function '''
    end = 100
    count = 0
    points = init_arr(end)
    gcds = gcd_table(end)
    squares = calc_squares(150)
    for x, y in product(points, repeat=2):
        interior = int(area(x, y)-line_lattice(gcds, x, y)/2) + 1
        sqr_root = interior**0.5
        if interior in squares:
            temp = (x[0] != x[1]) + (y[0] != y[1])
            count += 1 + temp + (temp == 2)
    print(count)

def init_arr(end):
    ''' Initialize array of points up to 'end' '''
    points = []
    for x in range(1, end+1):
        for y in range(1, x+1):
            points.append((x, y))
    return points

def gcd_table(end):
    ''' Create a lookup table for the 'gcd' of any pair of numbers between 1
    and 'end' '''
    gcds = dict()
    for a in range(1, end+1):
        for b in range(1, end+1):
            gcds[a, b] = gcd(a, b)
    return gcds

def calc_squares(end):
    ''' Return a set of all squares up to 'end**2' '''
    n = 1
    squares = set()
    while n <= end:
        squares.add(n**2)
        n += 1
    return squares

def area(x, y):
    ''' Find the area of the quadrilateral denoted by 'x' and 'y' '''
    return (sum(x) * sum(y)) / 2

# https://math.stackexchange.com/questions/628117/how-to-count-lattice-points-on-a-line
def line_lattice(gcds, x, y):
    ''' Find lattice points on lines with endpoints 'x' and 'y' '''
    return gcds[x[0], y[0]] + gcds[x[0], y[1]] + gcds[x[1], y[0]] + gcds[x[1], y[1]]

if __name__ == "__main__":
    main()
