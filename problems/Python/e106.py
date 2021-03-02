''' (A) represent the sum of elements in set A of size n. We shall call it a
special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true: S(B) =/= S(C); that is, sums of subsets cannot be
equal. If B contains more elements than C then S(B) > S(C). For this problem we
shall assume that a given set contains n strictly increasing elements and it
already satisfies the second rule. For n = 12, how many of the 261625 subset
pairs that can be obtained need to be tested for equality?  '''

from euler import powerset

def main():
    ''' Driver function '''
    print(num_need_equality_test(12))

def num_need_equality_test(n):
    ''' Determine how many pairs of subsets of any given set with 'n' elements
    need to be tested for equality to determine if the set is a special sum
    set.
        Any given set can be described using the first (smallest) term (or f)
    and the differences between successive terms (x1, x2, x3 ... x_(n-1)).
    Thus the sums of subsets can be expressed using only f and xs. When
    comparing the sums of two subsets, one can then simply look at how many
    times each difference is included in the sum (the fs subtract out). These
    counts can then be subtracted, resulting in the difference of the sums of
    the two subsets expressed solely in xs. Since one cannot deduce the
    relative values of the x terms, the equality test must be used if there are
    both negative and positive x values in the difference '''
    num = 0
    base = [x for x in range(n)]
    for a, b in subset_pairs(base):
        if len(a) != len(b):
            continue
        ax, bx = [0]*n, [0]*n
        for i, j in zip(a, b):
            ax[:i] = [x+1 for x in ax[:i]]
            bx[:j] = [x+1 for x in bx[:j]]
        signs = [False, False]
        for x0, x1 in zip(ax, bx):
            if x0 != x1:
                if signs[(x0>x1)-1]:
                    num += 1
                    break
                signs[x0>x1] = True
    return num

def subset_pairs(base_set):
    ''' Return all possible pairs of subsets of the powerset of 'base_set'
    excluding those that include the empty set '''
    pairs = []
    for s in powerset(base_set):
        if not s:
            continue
        index = base_set.index(s[0])
        comp = sorted(set(base_set[index+1:]) - set(s))
        pairs += [tuple(sorted((s, c))) for c in powerset(comp) if c]
    return pairs

if __name__ == "__main__":
    main()
