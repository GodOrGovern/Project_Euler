''' A spider, S, sits in one corner of a cuboid room and a fly, F, sits in
the opposite corner. There are up to three "shortest" path candidates for any
given cuboid and the shortest route doesn't always have integer length. Find
the least value of M such that the number of solutions first exceeds one
million '''

def main():
    ''' Driver function '''
    sqrs = gen_sqrs(10000)
    routes = []
    max_val = 3305873
    for n in range(1, 1300):
        if 2 * sqrs[n] > max_val:
            break
        for m in range(n+1, n+1000):
            route = sqrs[n] + sqrs[m]
            if route > max_val:
                break
            routes += [sqrs[n] + sqrs[m]]
    routes = sorted(routes)
    print(routes[10**6])
    print(routes[2060])

def gen_sqrs(end):
    ''' Generate all squares up to 'end**2' '''
    n = sqr = 1
    sqrs = [sqr]
    while n < end:
        sqr += 2*n + 1
        sqrs += [sqr]
        n += 1
    return sqrs

if __name__ == "__main__":
    main()
