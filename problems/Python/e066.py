''' Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained '''

from math import inf
from euler import convergent

def main():
    ''' Driver function '''
    cur_max = [0, 0]
    for n in range(1000):
        if int(n**0.5)**2 == n:
            continue
        converge = convergent(n, inf)
        d = next(converge)
        while d[0]**2 - n*d[1]**2 != 1:
            d = next(converge)
        if d[0] > cur_max[0]:
            cur_max = [d[0], n]
    print(cur_max[1])

if __name__ == "__main__":
    main()
