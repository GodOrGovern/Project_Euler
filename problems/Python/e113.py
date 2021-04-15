''' Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number; for example, 134468. Similarly if no digit
is exceeded by the digit to its right it is called a decreasing number; for
example, 66420. We shall call a positive integer that is neither increasing
nor decreasing a "bouncy" number; for example, 155349. How many numbers below
a googol (10**100) are not bouncy? '''

def main():
    ''' Driver function '''
    print(count_non_bouncy(100))

def count_non_bouncy(max_digits):
    ''' Return the number of positive non-bouncy numbers (NBNs) with up to
    max_digits digits '''
    pairs = [(first, last) for first in range(1, 10) for last in range(10)]
    # For a NBN (call it n) with start/end digits first and last,
    # new_pairs[first][last] contains a list of (first, last) pairs that
    # represent NBNs equal to n with one additional digit either prepended or
    # appended. Not all possible pairs for a given n are necessarily included
    # in the list to avoid redundancies
    new_pairs = [[[] for _ in range(10)] for _ in range(10)]
    for first, last in pairs:
        if first <= last:
            new_pairs[first][last] += [(d, last) for d in range(1, first+1)]
        if first >= last:
            # adding first!=last removes redundant NBN created when first == last
            new_pairs[first][last] += [(first, d) for d in range(last+(first!=last))]
    num_NBNs = 9
    # cur_pair_freq[first][last] is equal to the number of NBNs (for the
    # current digit length) with start/end digits equal to first/last
    cur_pair_freq = [[(a==b and a>0) for a in range(10)] for b in range(10)]
    for _ in range(max_digits-1):
        new_pair_freq = [[0 for _ in range(10)] for _ in range(10)]
        for first1, last1 in pairs:
            freq = cur_pair_freq[first1][last1]
            for first2, last2 in new_pairs[first1][last1]:
                new_pair_freq[first2][last2] += freq
                num_NBNs += freq
        cur_pair_freq = new_pair_freq
    return num_NBNs

if __name__ == "__main__":
    main()
