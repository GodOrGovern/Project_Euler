''' Define f(0)=1 and f(n) to be the number of different ways n can be
expressed as a sum of integer powers of 2 using each power no more than twice.
What is f(10**25)? '''

def main():
    ''' Driver function '''
    print(f(10**25))

def f(n):
    ''' Returns f(n) given the above definition of f. Uses dynamic programming
    based on the index(es) of 'on' bits in the binary representation of n '''
    # powers[x] is a list of tuples, each tuple representing the power of 2
    # denoted by the xth bit equal to 1 in bin(n) (from lowest to highest bit)
    # as the sums of powers of two, using each power at most twice. If the xth
    # on bit corresponds to 2**a and the x-1 on bit corresponds to 2**b then
    # only powers of 2 in the interval [2**b, 2**a] may be used (for x=0 it's
    # [2**0, 2**a]). Only the exponent of each power is stored in the tuples.
    powers = []
    prev_on_index = 0
    for index, bit in enumerate(bin(n)[:1:-1]):
        if bit == '1':
            power = [(index,)]
            for _ in range(index-prev_on_index):
                power += [(power[-1][0]-1, power[-1][0]-1) + power[-1][1:]]
            powers += [power]
            prev_on_index = index
    # Dynamic programming to count the number of ways to pick exactly one
    # tuple from each index of powers without any number appearing more than
    # twice between the tuples
    dp = [[1 for _ in powers[0]]] + [[0 for _ in power] for power in powers[1:]]
    for i in range(1, len(powers)):
        for num, prev in zip(dp[i-1], powers[i-1]):
            for j, cur in enumerate(powers[i]):
                combined = prev+cur
                if all((combined.count(x) <= 2) for x in set(combined)):
                    dp[i][j] += num
    return sum(dp[-1])

if __name__ == "__main__":
    main()
