''' Let S_m = (x_1, x_2, ... , x_m) be the m-tuple of positive real numbers
with x_1+x_2+...+x_m=m for which P_m=x_1*x_2**2*...*x_m**m is maximised. Find
Σ[P_m] for 2 ≤ m ≤ 15. '''

from functools import reduce
from operator import mul

def main():
    ''' Driver function '''
    print(sum(int(P(m)) for m in range(2, 16)))

def P(m):
    ''' Returns the maximum value of x_1*x_2**2*...*x_m**m for an m-tuple
    containing real numbers x_1,x_2,...,x_m with x_1+x_2+...+x_m=m. Does not
    work for m > 77 (returns 0.0) '''
    seq = [1] * m
    def maximize(i, j):
        ''' Transfers value from x_i (or seq[i-1]) to x_j (or seq[j-1]) using a
        binary search that converges on values of x_i and x_j that maximize
        x_i**i * x_j**j. The corresponding elements in seq are then updated '''
        best = seq[i-1]**i * seq[j-1]**j
        low, high = 0, seq[i-1]
        while low < high:
            diff = (low+high)/2
            new = (seq[i-1]-diff)**i * (seq[j-1]+diff)**j
            if new < best:
                high = diff-1e-10
            else:
                best = new
                low = diff+1e-10
        seq[i-1], seq[j-1] = seq[i-1]-diff, seq[j-1]+diff
    def get_score():
        ''' Returns x_1*x_2**2*...*x_m**m using current values of seq
        (x_1=seq[0], x_2=seq[1], x_m=seq[m-1]) '''
        return reduce(mul, [n**(i+1) for i,n in enumerate(seq)], 1)
    # Transfers value back and forth between x_m (or seq[m-1]) and the lower
    # m-1 values (or seq[:m-1]), converging on a value for P_m
    old_score, new_score = float("-inf"), 1
    while new_score-old_score != 0:
        for n in range(1, m):
            maximize(n, m)
            maximize(m, n)
        old_score, new_score = new_score, get_score()
    return new_score

if __name__ == "__main__":
    main()
