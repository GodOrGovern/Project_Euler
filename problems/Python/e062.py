''' Find the smallest cube for which exactly five permutations of its digits
are cube. '''

from collections import defaultdict

def main():
    ''' Keeps track of cubes by associating an identity with each number so
    that every number with the same digits has the same identity. The frequency
    of each identity is also tracked. Cubes are generated until an identity
    appears 5 times '''
    cubes = defaultdict(list)
    results = []
    num, length, identity = 0, 0, ''
    while not results or length >= len(identity):
        identity = ''.join(sorted(str(num**3)))
        cubes[identity].append(num)
        if len(cubes[identity]) == 5:
            results.append(identity)
            length = len(identity)
        num += 1
    result = min(results, key=lambda x: cubes[x][0])
    print(cubes[result][0]**3)

if __name__ == "__main__":
    main()
