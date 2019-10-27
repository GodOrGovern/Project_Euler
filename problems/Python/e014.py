''' Which starting number, under one million, produces the longest chain? '''

def main():
    ''' Removes all elements in sequence from nums, reducing the number of
    values to check '''
    nums = {x for x in range(1, 1000000)}
    maximum = [0, 0]
    while nums:
        num = nums.pop()
        sequence = collatz(num)
        length = len(sequence)
        if length > maximum[1]:
            maximum = [num, length]
        nums.difference_update(sequence)
    print(maximum[0])

def collatz(num):
    ''' Return collatz sequence starting with num '''
    sequence = []
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        elif num % 2 == 1:
            num = 3 * num + 1
        sequence.append(num)
    return sequence

if __name__ == "__main__":
    main()
