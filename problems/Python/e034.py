''' Find the sum of all numbers which are equal to the sum of the factorial of
their digits '''

from math import factorial

def main():
    ''' Driver function '''
    total = 0
    for x in range(10, 100000):
        if x == sum([factorial(int(n)) for n in str(x)]):
            total += x
    print(total)

if __name__ == "__main__":
    main()
