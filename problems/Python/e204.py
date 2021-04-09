''' We will call a positive number a generalised Hamming number of type n, if
it has no prime factor larger than n. How many generalised Hamming numbers of
type 100 are there which don't exceed 10**9? '''

from pyprimesieve import primes

def main():
    ''' Driver function '''
    print(len(general_hamming(10**9, 100)))

def general_hamming(end, high):
    ''' Return a set of all numbers (<= end) with prime factors not exceeding
    high '''
    hamming = {1}
    prev = {1}
    base = primes(high+1)
    while 2*min(prev) <= end:
        cur = set()
        for n in prev:
            for p in base:
                temp = n*p
                if temp > end:
                    break
                cur.add(temp)
        hamming.update(cur)
        prev = cur
    return hamming

if __name__ == "__main__":
    main()
