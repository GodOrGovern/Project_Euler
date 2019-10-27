''' How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000? '''

from math import gcd

def main():
    ''' Checks values between 1/3 and 1/2 for each denominator x. Keeps
    track of reduced form of each fraction (vals) '''
    vals = set()
    for x in range(1, 12001):
        for y in range(int(x/3)+1, int((x+1)/2)):
            div = gcd(x, y)
            vals.add((y//div, x//div))
    print(len(vals))

if __name__ == "__main__":
    main()
