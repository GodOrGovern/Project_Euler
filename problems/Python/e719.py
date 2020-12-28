''' We define an S-number to be a natural number, n, that is a perfect square
and its square root can be obtained by splitting the decimal representation of
n into 2 or more numbers then adding the numbers. Further we define T(N) to be
the sum of all S numbers n <= N. Find T(10^12) '''

def main():
    ''' Run with pypy otherwise it takes too long and/or crashes my laptop.
    Even with pypy it takes >10 minutes '''
    print(T(10**12))

def T(end):
    ''' Returns the sum of all S-numbers below 'end' '''
    return sum(n*n for n in range(4, round(end**0.5)+1) if n in digit_sums(n*n))

def digit_sums(n):
    ''' Return all values found by splitting the decimal representation of 'n'
    into 2 or more smaller numbers and then adding them together. '''
    digits = []
    while n:
        n, last = divmod(n, 10)
        digits += [last]
    sums = {(digits[-1],)}
    for d in digits[-2::-1]:
        temp = set()
        for s in sums:
            temp.update((s+(d,), s[:-1]+(s[-1]*10+d,)))
        sums = temp
    return map(sum, sums)

if __name__ == "__main__":
    main()
