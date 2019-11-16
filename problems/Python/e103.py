''' Let S(A) represent the sum of elements in set A of size n. We shall call
it a special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true: S(B) ≠ S(C); that is, sums of subsets cannot
be equal. If B contains more elements than C then S(B) > S(C). If S(A) is
minimised for a given n, we shall call it an optimum special sum set. Given
that A is an optimum special sum set for n = 7, find its set string '''

from itertools import chain, combinations

def main():
    ''' Driver function '''
    a = [20, 31, 37, 39, 40, 42, 45]
    print(is_special_set(a))

def is_special_set(base_set):
    ''' Determine if 'base_set' is an optimum special sum set '''
    bounds = boundaries(base_set)
    for i, n in enumerate(bounds[:-1]):
        if n[1] > bounds[i+1][0]:
            return False
    vals = set() 
    for subset in powerset(base_set): 
        total = sum(subset) 
        if total in vals: 
            return False
        vals.add(total)      
    return True

def boundaries(base_set):
    ''' Given 'base_set', determine the minimum and maximum values for
    sums of subsets of length 0 to 'len(base_set)'. Return as a list of
    lists, where each index represents a length and each sub-list has two
    values: the min and max '''
    base_set.sort()
    base_len = len(base_set)   
    bounds = [[0, 0] for _ in range(base_len + 1)]
    bounds[1] = [base_set[0], base_set[-1]]
    for n in range(2, base_len+1):
        bounds[n][0] = bounds[n-1][0] + base_set[n-1]
        bounds[n][1] = bounds[n-1][1] + base_set[-n]
    return bounds

def powerset(base_set):
    ''' Return the powerset of 'base_set' '''
    xs = list(base_set)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

if __name__ == "__main__":
    main()