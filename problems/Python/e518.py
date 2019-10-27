''' Let S(n) = Σa+b+c over all triples (a,b,c) such that: a, b, and c are prime
numbers; a < b < c < n; a+1, b+1, and c+1 form a geometric sequence. Find
S(10**8) '''

from collections import defaultdict
from pyprimesieve import primes as primes_to

def main():
    ''' Driver function '''
    end = 10**4
    print(progression(end))

def progression(end):
    ''' Build undirected graph where nodes are prime numbers and edges are
    the ratio between the larger prime and the smaller prime (plus 1 in both
    cases). Return the sum of nodes that are part of a geometric progression
    '''
    total = 0
    primes = primes_to(end)
    graph = defaultdict(dict)
    for i, p1 in enumerate(primes[:-1]):
        if graph[p1].keys():
            min_r = min(graph[p1].keys())
            max_r = max(graph[p1].keys())
        else:
            min_r = 1
            max_r = ((end-1) / (p1+1))**0.5
        for p2 in primes[i+1:]:
            r = (p2 + 1) / (p1 + 1)
            if (p2+1)*r > end and max_r < r or min_r > r:
                break
            if r in graph[p1]:
                total += p1 + p2 + graph[p1][r]
            else:
                graph[p1][r] = p2
            if r in graph[p2]:
                total += p1 + p2 + graph[p2][r]
            else:
                graph[p2][r] = p1
    return total

if __name__ == "__main__":
    main()
