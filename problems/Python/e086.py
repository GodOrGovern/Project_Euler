''' A spider, S, sits in one corner of a cuboid room and a fly, F, sits in
the opposite corner. There are up to three "shortest" path candidates for any
given cuboid and the shortest route doesn't always have integer length. Find
the least value of M such that the number of solutions first exceeds one
million '''

from euler import gen_triple
from gmpy2 import is_square

def main():
    ''' Driver function '''
    end = 100 
    count = 0
    for a, b in triple_legs(end):
        if b//2 <= a:
            count += b//2
            if a != b:
                count -= b - a - 1
        if b < end:
            count += a//2
        print(count, a, b)
    print(count)

def triple_legs(end):
    ''' Generates tuples where each tuple contains the values of the
    legs in a Pythagorean triple '''
    double_end = end * 2
    for t in gen_triple(double_end):
        t.sort()
        a1, b1 = a0, b0 = t[0], t[1]
        if a1 > end or b1 > double_end:
            break
        while a1 < end and b1 < double_end:
            yield (a1, b1)
            a1 += a0
            b1 += b0
                    
if __name__ == "__main__":
    main()