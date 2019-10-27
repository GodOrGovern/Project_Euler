''' A positive fraction whose numerator is less than its denominator is called
a proper fraction.  For any denominator, d, there will be d−1 proper fractions.
We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the
ratio of its proper fractions that are resilient. Find the smallest denominator
d, having a resilience R(d) < 15499/94744 '''

from flint import fmpz

def main():
    ''' Driver function '''
    minimum = 15499 / 94744
    denom = 2*3*5*7*11*13*17*19*23
    proper = denom - 1
    while int(fmpz.euler_phi(fmpz(denom))) / proper >= minimum:
        denom += 1
        proper += 1
    print(denom)

if __name__ == "__main__":
    main()
