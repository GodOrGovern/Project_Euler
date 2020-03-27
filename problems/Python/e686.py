''' Define p(L,n) to be the nth-smallest value of j such that the base 10
representation of 2**j begins with the digits of L. Find p(123,678910) '''

#from decimal import getcontext, Decimal
import mpmath as mp

def main():
    ''' Driver function '''
    mp.dps = 100
    start = mp.log10(1.23)
    end = mp.log10(1.24)
    log_2 = mp.log10(2)
    val = log_2
    count = 0
    exp = 0
    exp_prev = 0
    while count < 6:
        if start < val < end:
            print(exp-exp_prev)
            exp_prev = exp
            count += 1
        val += log_2
        val %= 1
        exp += 1
    print(exp)

1, 2, 1, 2, 1, 2, 1, 2, 1

def first_three(val):
    ''' Return the first three digits of '2**(val / log10(2))' '''
    return 1.23 < 10**(val % 1) < 1.24

if __name__ == "__main__":
    main()
