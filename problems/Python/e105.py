''' Let S(A) represent the sum of elements in set A of size n. We shall call
it a special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true: S(B) ≠ S(C); that is, sums of subsets cannot
be equal. If B contains more elements than C then S(B) > S(C). Using e105
text file with one-hundred sets containing seven to twelve elements (the two
examples given above are the first two sets in the file), identify all the
special sum sets, A1, A2, ..., A_k, and find the value of S(A1) + S(A2) + ...
+ S(A_k) '''

from itertools import chain, combinations
from euler import src, powerset

def main():
    ''' Driver function '''
    total = 0
    for s in load_data(src+'e105'):
        if is_optimum_special_set(s):
            total += sum(s)
    print(total)

def load_data(f_name):
    ''' Return data in 'f_name' as a list of lists '''
    lists = []
    with open(f_name) as data:
        for line in data:
            lists.append([int(n) for n in line.split(',')])
    return lists

def is_optimum_special_set(base_set):
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

if __name__ == "__main__":
    main()
