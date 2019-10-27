''' A positive integer n is called squarefree if no square of a prime divides n.
Find the sum of the distinct squarefree numbers in the first 51 rows of
Pascal's triangle '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    valid = set()
    for i, row in enumerate(pascal(51)):
        valid.update(n for n in row[:i//2 + 1] if squarefree(n))
    print(sum(valid))

def squarefree(n):
    ''' Check if 'n' is squarefree '''
    return not any(e > 1 for _, e in factorize(n))

def pascal(last):
    ''' Generator for Pascal's triangle, up to the 'last' row. It will always
    yield the first two rows '''
    yield [1]
    prev = [1, 1]
    yield prev
    row = 2
    while row < last:
        cur = [1] + [0] * (row - 1) + [1]
        for i, n in enumerate(prev[:-1]):
            cur[i+1] = prev[i+1] + n
        yield cur
        prev = cur
        row += 1

if __name__ == "__main__":
    main()
