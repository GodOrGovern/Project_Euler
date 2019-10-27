''' Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital '''

from itertools import permutations

def main():
    ''' Driver function '''
    result = set()
    perms = permutations([str(n) for n in range(1, 10)])
    for p in perms:
        prod = int(''.join(p[5:9]))
        mult = [int(''.join(p[0:2])) * int(''.join(p[2:5])),
                int(p[0]) * int(''.join(p[1:5]))]
        if prod in mult:
            result.add(prod)
    print(sum(result))

if __name__ == "__main__":
    main()
