''' Using all of the digits 1 through 9 and concatenating them freely to form
decimal integers, different sets can be formed. How many distinct sets
containing each of the digits one through nine exactly once contain only prime
elements? '''

from pyprimesieve import primes as primes_to
from pyprimesieve import factorize
from collections import defaultdict

def main():
    ''' Driver function '''
    print(count_sets(*get_valid()))

def count_sets(primes, digits, bits):
    def make_graph():
        ''' Return a graph where nodes are primes and edges connect primes that
        share no digits. Edges always point from a smaller prime to a larger prime '''
        graph = defaultdict(set)
        for i, primes1 in enumerate(primes):
            for p1 in primes1:
                for primes2 in primes[i:(8-i)]:
                    for p2 in primes2:
                        if (p1 >= p2) or (bits[p1] & bits[p2]):
                            continue
                        graph[p1].add(p2)
        return graph
    def find_path(cur, found, num_digits, paths):
        ''' Return the number of valid paths through 'graph' that exist starting at
        'cur'. 'found' and 'num_digits' are used to check validity of paths without
        tracking the actual primes. A path is considered valid if the first 9 bits
        of 'found' are 1 (ie 'found' == 2**9-1 == 511) '''
        if found == 511:
            return paths + 1
        for node in graph[cur]:
            if (digits[node] <= (9-num_digits)) and (not (bits[node] & found)):
                paths = find_path(node, found|bits[node], num_digits+digits[node], paths)
        return paths
    graph = make_graph()
    count = 0
    for prime in primes:
        count += sum(find_path(p, bits[p], digits[p], 0) for p in prime)
    return count

def get_valid():
    ''' This function returns:
            A list of lists ('valid_primes') where all primes in each sub-list
            are valid and have the same number of digits (starting at 1 digit
            in index 0). All valid primes are contained within the lists
            A dictionary ('valid_digits') with primes as keys and the number of
            digits in the corresponding keys as values.
            A dictionary ('valid_bits') with primes as keys and a bit
            representation of which digits (1-9) are in the corresponding key
            as values. A 1 in the nth bit means the key contains the digit n+1
        A prime is considered valid if it is < 10**8 and has no zeroes or
        repeating digits. '''
    primes = primes_to(10**8)
    valid_digits = defaultdict(int)
    valid_bits = defaultdict(int)
    valid_primes = [[] for _ in range(8)]
    shifts = [(1<<n) for n in range(10)]
    for n in primes:
        found = 0
        orig = n
        digits = 0
        while n:
            n, d = divmod(n, 10)
            if d == 0 or (shifts[d-1] & found):
                break
            found |= shifts[d-1]
            digits += 1
        else:
            valid_primes[digits-1] += [orig]
            valid_digits[orig] = digits
            valid_bits[orig] = found
    return valid_primes, valid_digits, valid_bits

if __name__ == "__main__":
    main()
