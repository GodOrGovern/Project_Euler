''' Let y_0, y_1, y_2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ y_i < 2^32, every value equally likely).  For the sequence x_i the
following recursion is given: x_0 = 0 and x_i = x_i-1| y_i-1, for i > 0. ( | is
the bitwise-OR operator) It can be seen that eventually there will be an index
N such that x_i = 2^32 -1 (a bit-pattern of all ones) for all i ≥ N. Find the
expected value of N. Give your answer rounded to 10 digits after the decimal
point '''

from random import randint

def main():
    ''' Driver function '''
    iters = 10**5
    print(sum(simulate() for _ in range(iters)) / iters)

def simulate():
    ''' Return the index at which 'x' becomes '2**32-1' '''
    x = 0
    index = 0
    end = 2**32 - 1
    while x != end:
        x |= randint(0, end)
        index += 1
    return index

if __name__ == "__main__":
    main()
