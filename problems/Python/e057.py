''' In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator? '''

from math import log10
from euler import convergent

def main():
    ''' Driver function '''
    count = 0
    for numer, denom in convergent(2, 1000):
        if int(log10(numer)) > int(log10(denom)):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
