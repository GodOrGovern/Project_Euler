''' In the following equation x, y, and n are positive integers. 1/x + 1/y =
1/n. What is the least value of n for which the number of distinct solutions
exceeds one-thousand? '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    n = 1
    while factor_pairs_square(n) < 1000:
        n += 1
    print(n)

def factor_pairs_square(num):
    ''' Find the number of factor pairs of 'num**2' '''
    pairs = 1
    for _, e in factorize(num):
        pairs *= 2*e + 1
    return (pairs + (pairs % 2)) // 2

if __name__ == "__main__":
    main()
