''' How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000? '''

from euler import totients_to

def main():
    ''' The sum of totient values up to n gives the number of reduced proper
    fractions with denominator less than or equal to n '''
    print(sum(totients_to(10**6)[1:]))

if __name__ == "__main__":
    main()
