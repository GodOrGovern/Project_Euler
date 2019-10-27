''' Find the first four consecutive integers to have four distinct prime
factors each. What is the first of these numbers? '''

from pyprimesieve import factorize

def main():
    ''' Brute-forces the answer by finding prime factors of test until n
    adjacent numbers with n distinct primes are found '''
    test = 2
    count = 0
    n = 4
    while count < n:
        count += 1
        if len(factorize(test)) != n:
            count = 0
        test += 1
    print(test - n)

if __name__ == "__main__":
    main()
