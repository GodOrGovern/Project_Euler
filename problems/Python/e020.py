''' Find the sum of the digits in the number 100! '''

from math import factorial

def main():
    ''' Driver function '''
    print(sum([int(x) for x in str(factorial(100))]))

if __name__ == "__main__":
    main()
