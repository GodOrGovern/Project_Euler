''' We shall define an almost equilateral triangle to be a triangle for which
two sides are equal and the third differs by no more than one unit. Find the
sum of the perimeters of all almost equilateral triangles with integral side
lengths and area and whose perimeters do not exceed one billion '''

from gmpy2 import is_square

def main():
    ''' Driver function '''
    valid = []
    base1, base2 = 7, 11
    for n in range(2, 10**7):
        inc1 = 6*n + 1
        inc2 = 6*n + 5
        if is_square(base1) and check_area(n+1, base1):
            valid.append((n, n+1))
        if is_square(base2) and check_area(n-1, base2):
            valid.append((n, n-1))
        base1 += inc1
        base2 += inc2
    print(valid)

def check_area(base, part_area):
    ''' Calculate the remainder of the area and check if it is an integer.
    Return True if yes, else False '''
    area = (base / 4) * part_area**0.5
    return area.is_integer()

if __name__ == "__main__":
    main()
