''' A row measuring n units in length has blocks with a minimum length of m
units placed on it, such that any two blocks (which are allowed to be different
lengths) are separated by at least one square. Let the fill-count function,
F(m, n), represent the number of ways that a row can be filled.  For m = 50,
find the least value of n for which the fill-count function first exceeds one
million. '''

from euler import tilings

def main():
    ''' Driver function '''
    # Binary search
    target = 10**6
    low, high = 50, 500
    while low < high:
        mid = (low + high) // 2
        if tilings(mid, min_length=50, min_dist=1, mix_lengths=True) > target:
            high = mid-1
        else:
            low = mid+1
    print(low)

if __name__ == "__main__":
    main()
