''' Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum '''

def main():
    ''' Driver function '''
    sum_square = sum([x**2 for x in range(1, 101)])
    square_sum = sum([x for x in range(1, 101)])**2
    print(square_sum - sum_square)

if __name__ == "__main__":
    main()
