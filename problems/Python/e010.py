''' Find the sum of all the primes below two million '''

from pyprimesieve import primes_sum

def main():
    ''' Driver function '''
    print(primes_sum(2000000))

if __name__ == "__main__":
    main()
