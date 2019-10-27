''' Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of
D? '''

from math import sqrt

def main():
    ''' Progressively filters the possibilities until an answer is found '''
    pent = []
    c = 1
    min_diff = 0
    while not min_diff:
        cur = c*(3*c - 1)//2
        calc_all = [cur-p for p in pent]
        calc_pent = [n for n in calc_all if is_pent(n)]
        orig = [cur-p for p in calc_pent]
        calc_all = [cur+p for p in orig]
        calc_pent = [n for n in calc_all if is_pent(n)]
        if calc_pent:
            min_diff = min([2*cur-p for p in calc_pent])
        pent.append(cur)
        c += 1
    print(min_diff)

def is_pent(n):
    ''' Determine if n is a pentagonal number '''
    if not (sqrt(1 + 24*n) - 5) % 6:
        return True
    return False

if __name__ == "__main__":
    main()
