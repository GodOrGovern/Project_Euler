''' How many ways can a row measuring fifty units in length be filled with
blocks of minimum length 3 such that any two blocks (which are allowed to be
different lengths) are separated by at least one square? '''

from euler import tilings

def main():
    ''' Driver function '''
    # One is added to account for tiling with no blocks
    print(tilings(50, min_length=3, min_dist=1, mix_lengths=True)+1)

if __name__ == "__main__":
    main()
