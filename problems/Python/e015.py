''' How many such routes are there through a 20×20 grid? '''

from sympy import binomial

def main():
    ''' Equivalent to 40 choose 20 '''
    print(binomial(40, 20))

if __name__ == "__main__":
    main()
