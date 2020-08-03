''' Each of the six faces on a cube has a different digit (0 to 9) written on
it; the same is done to a second cube. By placing the two cubes side-by-side in
different positions we can form a variety of 2-digit numbers.  In fact, by
carefully choosing the digits on both cubes it is possible to display all of
the square numbers below one-hundred.  However, for this problem we shall allow
the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8,
9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed;
otherwise it would be impossible to obtain 09.  How many distinct arrangements
of the two cubes allow for all of the square numbers to be displayed? '''

from itertools import combinations

def main():
    ''' Driver function '''
    result = 0
    combs = [n for n in combinations(range(10), 6)]
    for i, c1 in enumerate(combs):
        for c2 in combs[i:]:
            result += valid(c1, c2)
    print(result)

def valid(c1, c2):
    ''' Check if 'c1' and 'c2' can form all squares '''
    combs = [[0,1],[0,4],[0,6],[1,6],[2,5],[3,6],[4,6],[6,4],[8,1]]
    for c in combs:
        if 6 in c:
            i = 6 == c[0]
            if not (((6 in c1 or 9 in c1) and c[i] in c2) or
                    (c[i] in c1 and (6 in c2 or 9 in c2))):
                return False
        elif not ((c[0] in c1 and c[1] in c2) or (c[1] in c1 and c[0] in c2)):
            return False
    return True

if __name__ == "__main__":
    main()
