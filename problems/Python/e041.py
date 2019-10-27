''' What is the largest n-digit pandigital prime that exists? '''

from sympy.ntheory import isprime

def main():
    ''' Driver function '''
    start = 7
    result = None
    while not result and start > 2:
        result = pan_prime(start)
        start -= 1
    print(result)

def pan_prime(n):
    ''' Find the largest pandigital prime number of length n. If none
    exist, return None '''
    elements = [x for x in range(n, 0, -1)]
    perm = int(''.join(map(str, elements)))
    low_bound = int(''.join(map(str, elements[::-1])))
    while not isprime(perm):
        if perm == low_bound:
            return None
        next_perm(elements)
        perm = int(''.join(map(str, elements)))
    return perm

def next_perm(elements):
    ''' Get next lexicographic permutation of elements in descending order '''
    last_index = len(elements) - 1
    if last_index < 1:
        return None
    high = last_index - 1
    while high >= 0 and elements[high] <= elements[high + 1]:
        high -= 1
    # if there is no lower permutation, return to the first one
    if high < 0:
        return elements.reverse()
    low = last_index
    while low > high + 1 and elements[low] >= elements[high]:
        low -= 1
    elements[high], elements[low] = elements[low], elements[high]
    elements[high+1:] = elements[high+1:][::-1]
    return elements

if __name__ == "__main__":
    main()
