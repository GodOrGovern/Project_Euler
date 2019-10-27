''' What is the largest prime factor of the number 600851475143? '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    print(factorize(600851475143)[-1][0])

if __name__ == "__main__":
    main()
