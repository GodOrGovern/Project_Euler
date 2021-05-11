''' How many different ways can the tiles in a row measuring fifty units in
length be replaced with blocks of length 2, 3, and 4 if lengths cannot be mixed
and at least one block must be used? '''

from euler import tilings

def main():
    ''' Driver function '''
    print(sum(tilings(50, l) for l in [2, 3, 4]))

if __name__ == "__main__":
    main()
