''' How many, not necessarily distinct, values of nCr for 1 ≤ n ≤ 100, are
greater than one-million? '''

from sympy import binomial

def main():
    ''' Print count '''
    count = 0
    for n in range(1, 101):
        count += vals_above_mil(n)
    print(count)

def vals_above_mil(n):
    ''' Return how many values of the function binomial exceed one million, where
    'r' is all possible values given 'n' '''
    for r in range(1, n // 2):
        if binomial(n, r) > 1000000:
            return n - 2*r + 1
    return 0

if __name__ == "__main__":
    main()
