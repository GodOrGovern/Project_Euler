''' Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits. '''

def main():
    ''' Brute-force solution '''
    base = 1
    mult = 2
    while mult < 7:
        mult = 2
        digits = set(str(base))
        while set(str(mult*base)) == digits:
            mult += 1
        base += 1
    print(base-1)

if __name__ == "__main__":
    main()
