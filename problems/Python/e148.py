''' Find the number of entries which are not divisible by 7 in the first one
billion (10^9) rows of Pascal's triangle '''

def main():
    ''' Driver function '''
    '''
    count = 0
    for row in pascal_mod_seven(10**2):
        count += sum(n > 0 for n in row)
    '''
    for row in pascal_mod(10**2, 6):
        for n in row:
            if n:
                print(0, end='')
            else:
                print(1, end='')
        print()

def pascal_mod(row, mod):
    ''' Generator for the first 'row' rows of Pascal's triangle. Numbers are
    only kept track of modulo 'mod' '''
    prev = [1, 1]
    yield [1]
    yield prev
    length = 2
    while length < row:
        cur = prev + [1]
        for i, n in enumerate(prev):
            if i in {0, length}:
                continue
            cur[i] = (prev[i-1] + prev[i]) % mod
        yield cur
        prev = cur
        length += 1

if __name__ == "__main__":
    main()
