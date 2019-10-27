''' The radical of n, rad(n), is the product of the distinct prime factors of
n. Let E(k) be the kth element in the sorted n column. If rad(n) is sorted for
1 ≤ n ≤ 100000, find E(10000) '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    end = 100000
    nums = []
    for n in range(1, end+1):
        nums.append((rad(n), n))
    nums.sort()
    print(nums[9999][1])

def rad(n):
    ''' Find the radical of 'n' '''
    total = 1
    for p, _ in factorize(n):
        total *= p
    return total

if __name__ == "__main__":
    main()
