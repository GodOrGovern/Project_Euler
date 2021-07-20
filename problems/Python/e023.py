''' Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers '''

import numpy as np
from sympy import divisors

def main():
    ''' Driver function '''
    # All integers greater than 20161 can be written as the sum of two
    # abundant numbers
    abundant = get_abundant(20161)
    print(no_abundant_sum(abundant, 20161))

def get_abundant(end):
    ''' Return an array of all abundant numbers below 'end' '''
    abundant = np.array([], dtype=int)
    for num in range(1, end + 1):
        if sum(divisors(num)[:-1]) > num:
            abundant = np.append(abundant, num)
    return abundant

def no_abundant_sum(abundant, end):
    ''' Return the sum of all integers which cannot be written as the sum of
    two abundant numbers '''
    success = []
    for num in range(1, end + 1):
        diff = num - abundant[abundant < num]
        if np.intersect1d(diff, abundant).size == 0:
            success.append(num)
    return sum(success)

if __name__ == "__main__":
    main()
