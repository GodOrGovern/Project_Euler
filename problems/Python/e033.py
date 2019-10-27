''' The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s. We shall consider fractions like,
30/50 = 3/5, to be trivial examples. There are exactly four non-trivial
examples of this type of fraction, less than one in value, and containing two
digits in the numerator and denominator. If the product of these four fractions
is given in its lowest common terms, find the value of the denominator. '''

from math import gcd

def main():
    ''' Bruteforce all possible configurations given the parameters '''
    frac = (1, 1)
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(x+1, 10):
                if (10*x+z)/(10*z+y) == x / y:
                    frac = (frac[0]*x, frac[1]*y)
    print(frac[1]//gcd(frac[0], frac[1]))

if __name__ == "__main__":
    main()
