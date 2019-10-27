''' Let p(n) represent the number of different ways in which n coins can be
separated into piles. Find the least value of n for which p(n) is divisible by
one million '''

# Heavily influenced by
# https://math.stackexchange.com/questions/2675382/calculating-integer-partitions
def main():
    ''' Uses Euler's Pentagonal Number Theorem to recursively calculate
    progressively larger values of p(n) until a multiple of 10**6 is found '''
    partition = [1]
    pentagonal = []
    n = 0
    while partition[n] % 10**6:
        n += 1
        partition.append(0)
        pentagonal.extend([n*(3*n-1)//2, -n*(-3*n-1)//2])
        for i, p in enumerate(pentagonal):
            co = -1 if i//2 % 2 else 1
            if n-p >= 0:
                partition[n] += co*partition[n-p]
            else:
                break
    print(n)

if __name__ == "__main__":
    main()
