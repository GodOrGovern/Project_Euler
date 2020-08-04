''' If we are presented with the first k terms of a sequence it is impossible
to say with certainty the value of the next term, as there are infinitely many
polynomial functions that can model the sequence.  Suppose we were only given
the first two terms of this sequence. Working on the principle that "simple is
best" we should assume a linear relationship and predict the next term to be 15
(common difference 7). Even if we were presented with the first three terms, by
the same principle of simplicity, a quadratic relationship should be assumed.
We shall define OP(k, n) to be the nth term of the optimum polynomial
generating function for the first k terms of a sequence. It should be clear
that OP(k, n) will accurately generate the terms of the sequence for n ≤ k, and
potentially the first incorrect term (FIT) will be OP(k, k+1); in which case we
shall call it a bad OP (BOP).  As a basis, if we were only given the first term
of sequence, it would be most sensible to assume constancy; that is, for n ≥ 2,
OP(1, n) = u1.  Consider the following tenth degree polynomial generating
function: f(n) = 1 − n + n2 − n3 + n4 − n5 + n6 − n7 + n8 − n9 + n10 Find the
sum of FITs for the BOPs. '''

def main():
    ''' Driver function '''
    fit_sum = 0
    f = lambda n: 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    for n in range(1, 11):
        seq = [f(n) for n in range(1, n+1)]
        while seq[-1] == f(n):
            term = next_term(seq)
            seq += [term]
            n += 1
        fit_sum += term
    print(fit_sum)

def next_term(seq):
    ''' Return the next value of the simplest polynomial that could generate the
    terms of 'seq' '''
    diff = [seq]
    while len(diff[-1]) > 1 and not all(d == diff[-1][0] for d in diff[-1]):
        diff += [[b-a for a, b in zip(diff[-1], diff[-1][1:])]]
    return sum(d[-1] for d in diff)

if __name__ == "__main__":
    main()
