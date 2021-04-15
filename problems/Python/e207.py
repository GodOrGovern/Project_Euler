''' For some positive integers k, there exists an integer partition of the form
4**t = 2**t + k, where 4**t, 2**t, and k are all positive integers and t is a
real number. Partitions where t is also an integer are called perfect. For any
m >= 1 let P(m) be the proportion of such partitions that are perfect with k <=
m. Find the smallest m for which P(m) < 1/12345  '''

from math import log, sqrt

def main():
    ''' Driver function '''
    print(find_lowest_m(1/12345))

def find_lowest_m(target):
    ''' Returns the lowest value of m such that the proportion of perfect
    partitions (out of all partitions) with k <= m is less than target '''
    # Returns number of partitions below n. Found by treating 2**t as a
    # variable (x) and solving the quadratic x**2=x-n
    num_all = lambda n: (1+(1+4*n)**0.5)//2 - 1
    # Returns number of perfect partitions below n
    num_perfect = lambda n: log(sqrt(n), 2)//1
    P = lambda n: num_perfect(n) / num_all(n)
    # Find an upper bound
    high = 5
    while P(high) >= target:
        high *= 2
    # Generate all k up to that bound
    n = 2
    k = [2]
    while k[-1] <= high:
        k.append(n*(n+1))
        n += 1
    # Binary search on k
    low, high = 0, len(k)-1
    cur = (low + high) // 2
    while low < high:
        if P(k[cur]) >= target:
            low = cur+1
            cur = (cur + high) // 2
        else:
            high = cur-1
            cur = (low + cur) // 2
    return k[cur]

if __name__ == "__main__":
    main()
