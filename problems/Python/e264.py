''' Consider all the triangles having: All their vertices on lattice points,
Circumcentre at the origin, Orthocentre at (5, 0). Find all such triangles with
a perimeter <= 10^5. Enter as your answer the sum of their perimeters rounded
to four decimal places. '''

from bisect import bisect_left
from collections import defaultdict

def main():
    ''' Takes about 30 minutes to run '''
    vertices = get_vertices(20000)
    valid = get_valid(vertices)
    print(sum(perimeter(a, b, c) for a, b, c in valid))

def perimeter(a, b, c):
    ''' Find the perimeter of the triangle with vertices at '(a, b, c)' '''
    def distance(p, q):
        ''' Find the euclidean distance between 2D points 'p' and 'q' '''
        return ((p[0]-q[0])**2 + (p[1]-q[1])**2)**0.5
    return distance(a, b) + distance(a, c) + distance(b, c)

def get_vertices(end):
    ''' 'vertices[d]' lists all possible possible '(x, y), (y, x)' pairs
    satisfying 'x**2 + y**2 == d' and 'd % 10 == 5' '''
    sqr = [x*x for x in range(end)]
    vertices = defaultdict(list)
    # Only certain (x, y) pairs produce squares which add to a number ending in 5
    # 'corr[a % 10]' contains all 'b % 10' such '(a**2 + b**2) % 10 == 5'
    # If 'a < b' then 'a' is not included in 'corr[b]'
    corr = [(5,), (2, 8), (9,), (4, 6), (7,), None, (7,), None, (9,)]
    for a in [0, 1, 2, 3, 4, 6, 8]:
        for b in corr[a]:
            for x in range(a, end, 10):
                for y in range(b, end, 10):
                    vertices[sqr[x]+sqr[y]] += [(x, y), (y, x)]
    return vertices

def get_valid(vertices):
    ''' Finds all triplets of distinct points '(x1, y1), (x2, y2), (x3, y3)'
    in 'vertices' such that 'x1**2 + y1**2 == x2**2 + y2**2 == x3**2 +
    y3**2', 'x1+x2+x3 == 5', and 'y1+y2+y3 == 0'. Assumes that 'vertices[d]'
    contains all positive '(x, y),(y, x)' pairs such that 'x**2 + y**2 == d' '''
    valid = set()
    sqr = [x*x for x in range(100000)]
    sqrs = set(sqr)
    for d, pairs in vertices.items():
        if len(pairs) == 2:
            continue
        for i, (x1, y1) in enumerate(pairs):
            for x2, y2 in pairs[i:]:
                for ix1, ix2 in [(x1, x2), (-x1, x2), (x1, -x2), (-x1, -x2)]:
                    x3 = 5-ix1-ix2
                    if d-sqr[abs(x3)] in sqrs:
                        y3 = bisect_left(sqr, d-sqr[abs(x3)])
                        for iy1, iy2 in [(y1, y2), (-y1, y2), (y1, -y2), (-y1, -y2)]:
                            a, b, c = (ix1, iy1), (ix2, iy2), (x3, y3)
                            if -iy1-iy2 == y3 and a != b and a != c and b != c:
                                valid.add(tuple(sorted((a, b, c))))
    return valid

if __name__ == "__main__":
    main()
