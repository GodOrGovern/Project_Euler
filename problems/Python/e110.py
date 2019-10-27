''' In the following equation x, y, and n are positive integers. 1/x + 1/y =
1/n. What is the least value of n for which the number of distinct solutions
exceeds four million? '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    base = 1260
    n = 1260
    while factor_pairs_square(n) < 10**4:
        n += base
    print(n)

def factor_pairs_square(num):
    ''' Find the number of factor pairs of 'num**2' '''
    pairs = 1
    for _, e in factorize(num):
        pairs *= 2*e + 1
    return (pairs + (pairs % 2)) // 2

if __name__ == "__main__":
    main()
