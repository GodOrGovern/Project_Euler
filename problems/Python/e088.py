''' A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.  For a given set of size,
k, we shall call the smallest N with this property a minimal product-sum
number.  What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    end = 12000
    factors = dict()
    for n in range(2, 2*end+1):
        factors[n] = factorization(n)
    print(sum({minimal_prod_sum(n, factors) for n in range(2, end+1)}))

def minimal_prod_sum(n, factors):
    ''' Return the minimal product sum number with set of size 'n' '''
    val = 2*n
    for a in range(n, 2*n):
        for f in factors[a]:
            if sum(f) + n - len(f) == a:
                val = a
                break
        if val < 2*n:
            break
    return val

def factorization(n):
    ''' Return a set with all possible factorizations of 'n' '''
    prev = [tuple(p for p, e in factorize(n) for _ in range(e))]
    factors = len(prev[0])
    total = {prev[0]}
    for c in range(factors-2):
        cur = set()
        for p in prev:
            for i, a in enumerate(p):
                for j, b in enumerate(p[i+1:]):
                    cur.add(tuple(sorted((a*b,)+p[:i]+p[i+1:i+j+1]+p[i+j+2:])))
        prev = cur
        total.update(cur)
    return total



if __name__ == "__main__":
    main()
