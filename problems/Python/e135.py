''' The positive integers, x, y, and z, are consecutive terms of an arithmetic
progression. Given that n is a positive integer, for how many values of n less
than fifty million does the equation x^2 - y^2 - z^2 = n (x > y > z) have
exactly one solution? '''

from collections import defaultdict

def main():
    ''' Driver function '''
    print(get_num_n(10**6, 10))

def get_num_n(end, num):
    ''' Return the number of values of n (positive integer) below 'end' for
    which there ar exactly num triples (x, y, z), where x, y, and z are
    consecutive positive terms in an arithmetic sequence, satisfying the
    equation x^2 - y^2 - z^2 = n.
    If z is the lowest term in the sequence and d is the difference between
    consecutive terms, the equation can be re-written in terms of only three
    variables (d, z, n) instead of 4:
        z=z, y=z+d, x=z+2d therefore x^2-y^2-z^2=(z+2d)^2-(z+d)^2-z^2
        The right-side simplifies to 3d^2+2dz-z^2 which factors to (3d-z)(d+z).
    If we set f=3d-z and g=d+z, z can be expressed as z=3d-f allowing g to be
    expressed as 4d-f, making the new equation f(4d-f)=n. If d is held
    constant, bounds for f can be found using the quadratic formula and the
    fact that z>0. All possible values of 'd' (range for 'd' is [1, end/4]) and
    'f' are then iterated over, with the number of solutions for the
    corresponding 'n' values being tracked in 'counts' ('counts[t]' gives the
    number of solutions for n=t) '''
    def counts_over_range(start, stop):
        ''' Increment the counter for all n that can be formed given 'd' (in
        the equation f*(4d-f)=n) and the range [start, stop) for 'f'. '''
        temp = 4*d
        val = start*(temp-start)
        for f in range(start, stop):
            if 0 < val < end:
                counts[val] += 1
            #Difference between successive 'vals' is added instead of re-computing
            val += temp-2*f-1
    #Found using radicand from quadratic solution (d^2 >= end/4)
    turn = int(end**0.5 / 2) + 1
    counts = defaultdict(int)
    for d in range(1, turn):
        counts_over_range(1, 3*d)
    for d in range(turn, end//4 + 1):
        #Solution to quadratic for n=end is t1 +/- t2
        t1, t2 = 2*d, int(2*(d*d - end//4)**0.5)
        if t1-t2 > 0:
            counts_over_range(1, t1-t2)
        counts_over_range(t1+t2, 3*d)
    return sum(c==num for c in counts.values())

if __name__ == "__main__":
    main()
