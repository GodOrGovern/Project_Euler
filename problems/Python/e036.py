''' Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2. '''

def main():
    ''' Find sum of numbers that are palindromic in base 10 and base 2 '''
    count = 0
    for x in range(0, 1000000):
        binary = bin(x)
        num = str(x)
        if binary[2:] == binary[:1:-1] and num == num[::-1]:
            count += x
    print(count)


if __name__ == "__main__":
    main()
