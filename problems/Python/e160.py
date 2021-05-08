''' For any N, let f(N) be the last five digits before the trailing zeroes in
N!. Find f(1,000,000,000,000) '''

from math import log

def main():
    ''' Driver function '''
    print(last_digits(10**12, 5))

def last_digits(num, digits):
    ''' Find the last digits before the trailing zeroes in factorial(num)
    (equivalent to f in problem description when digits=5). Based on
    https://stackoverflow.com/a/45225874/9352652 '''
    mod = 10**digits
    twos = sum(num//(2**n) for n in range(1, int(log(num,2))+1))
    fives = sum(num//(5**n) for n in range(1, int(log(num,5))+1))
    val = pow(2, twos-fives, mod)
    # prod[n] is the product of all numbers <= n relatively prime to 2 and 5
    prod = [1]
    for n in range(1, mod):
        prod += [(prod[-1] if (n%2==0 or n%5==0) else n*prod[-1]) % mod]
    for n in mults_of_nums([2, 5], num):
        val = (val * prod[(num//n) % mod]) % mod
    return val

def mults_of_nums(nums, end):
    ''' Return a set containing all numbers <= end whose prime factors are a
    subset of nums (including 1 for the empty set) '''
    nums = sorted(nums)
    # sets are used because this process generates duplicates
    mults = {1}
    prev = {1}
    while min(nums)*min(prev) <= end:
        cur = set()
        for p in prev:
            for n in nums:
                temp = n*p
                # nums needs to be sorted for this optimization
                if temp > end:
                    break
                cur.add(temp)
        mults.update(cur)
        prev = cur
    return mults

if __name__ == "__main__":
    main()
