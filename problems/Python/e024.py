''' What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9? '''

def main():
    ''' Driver function '''
    elements = [x for x in range(0, 10)]
    count = 1
    while count < 1000000:
        next_perm(elements)
        count += 1
    print(''.join(str(x) for x in elements))

def next_perm(elements):
    ''' Return next lexicographic permutation of elements '''
    last_index = len(elements) - 1
    if last_index < 1:
        return None
    low = last_index - 1
    while low >= 0 and elements[low] >= elements[low + 1]:
        low -= 1
    # if there is no greater permutation, return to the first one
    if low < 0:
        return elements.reverse()
    high = last_index
    while high > low + 1 and elements[high] <= elements[low]:
        high -= 1
    elements[low], elements[high] = elements[high], elements[low]
    elements[low+1:] = elements[low+1:][::-1]
    return elements

if __name__ == "__main__":
    main()
