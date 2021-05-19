''' Find the smallest x + y + z with integers x > y > z > 0 such that x+y, x-y,
x+z, x−z, y+z, y−z are all perfect squares '''

from collections import defaultdict

def main():
    ''' Driver function '''
    print(sum(find_x_y_z()))

def find_x_y_z():
    ''' Find the lowest value of x+y+z such that x+y, x-y, x+z, x-z, y+z, and
    y-z are perfect squares '''
    # Derived from setting x+y=a, x-y=b, x+z=c, x-z=d, y+z=e, y-z=f where
    # a,b,c,d,e,f are perfect squares
    n = 1
    a = n*n
    sqrs = {a}
    sum_sqrs = defaultdict(set)
    diff_sqrs = defaultdict(set)
    while True:
        a += 2*n+1
        n += 1
        for b in sqrs:
            if a+b % 2 == 1:
                continue
            for (c, d) in sum_sqrs[a+b]:
                x, y, z = (a+b)//2, (a-b)//2, (c-d)//2
                if (y+z in sqrs) and (y-z in sqrs):
                    return (x, y, z)
            sum_sqrs[a+b].add((a, b))
            diff_sqrs[a-b].add((a, b))
        sqrs.add(a)

if __name__ == "__main__":
    main()
