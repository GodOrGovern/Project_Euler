''' Let y_0, y_1, y_2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ y_i < 2^32, every value equally likely).  For the sequence x_i the
following recursion is given: x_0 = 0 and x_i = x_{i-1}| y_{i-1}, for i > 0. (
| is the bitwise-OR operator) It can be seen that eventually there will be an
index N such that x_i = 2^32-1 (a bit-pattern of all ones) for all i ≥ N. Find
the expected value of N. Give your answer rounded to 10 digits after the
decimal point '''

def main():
    ''' 1-0.5**n is the probability that a single bit is 1 after being OR'ed
    with n ys. As all bits are independent, the probability of all bits being 1
    after being OR'ed with n ys is (1-0.5**n)**32. We will call this p(n). The
    probability of x first equalling 2**32-1 (all bits 1) after n turns is
    p(n)-p(n-1). Expected value is thus the sum n*(p(n)-p(n-1)) for n = 1
    to infinity (or however many values are needed to guarantee accuracy to 10
    decimal places, in this case 50 are used) '''
    p = lambda n: (1 - 0.5**n)**32
    print(sum(n*(p(n)-p(n-1)) for n in range(1, 50)))

if __name__ == "__main__":
    main()
