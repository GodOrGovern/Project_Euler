''' Every positive integer can be uniquely written as a sum of nonconsecutive
terms of the Fibonacci sequence.  Such a sum is called the Zeckendorf
representation of the number. For any integer n>0, let z(n) be the number of
terms in the Zeckendorf representation of n.  Find ∑z(n) for 0<n<10**17. '''

from euler import fib

def main():
    ''' Driver function '''
    end = 10**7
    fib_nums = get_fib_nums(end)
    fib_nums_set = set(fib_nums)
    fib_len = [0] * end
    total = 0
    index = 0
    for n in range(1, end):
        if n in fib_nums_set:
            fib_len[n] = 1
            index += 1
        else:
            fib_len[n] = 1 + fib_len[n-fib_nums[index]]
        total += fib_len[n]
    print(total)

def get_fib_nums(end):
    ''' Return a list of all Fibonacci numbers up to 'end' '''
    nums = []
    for n in fib():
        if n > end:
            break
        nums += [n]
    return nums

if __name__ == "__main__":
    main()
