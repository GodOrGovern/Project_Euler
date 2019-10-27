''' We shall define a square lamina to be a square outline with a square "hole"
so that the shape possesses vertical and horizontal symmetry. Let N(n) be the
number of t ≤ 10**6 such that t is type L(n). What is ∑N(n) for 1 ≤ n ≤ 10? '''

def main():
    ''' Driver function '''
    print(sum(1 for n in distinct_laminae(10**6) if 1 <= n <= 10))

def distinct_laminae(max_tiles):
    ''' Keeps track of how many distinct laminae can be made using up to
    'max_tiles' tiles for each number of tiles '''
    count = [0 for n in range(max_tiles+1)]
    s = 3
    perimeter = 8
    while perimeter <= max_tiles:
        count = laminae_num(s, max_tiles, count)
        perimeter += 4
        s += 1
    return count

def laminae_num(s, max_tiles, count):
    ''' For each lamina that can be formed with shortest side-length 's' and
    using up to 'max_tiles' tiles, the index in 'count' with its number of
    tiles is incremented by one '''
    perimeter = 4*s - 4
    total_tiles = perimeter
    while total_tiles <= max_tiles:
        count[total_tiles] += 1
        perimeter += 8
        total_tiles += perimeter
    return count

if __name__ == "__main__":
    main()
