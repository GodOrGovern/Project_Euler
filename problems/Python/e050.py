''' Which prime, below one-million, can be written as the sum of the most
consecutive primes? '''

from primesieve import primes as primes_to

def main():
    ''' Driver function '''
    primes = primes_to(1000000)
    old_range, old_max = low_bound(primes)
    new_range, new_max = check_all(old_range, primes)
    if new_range > old_range:
        print(new_max)
    else:
        print(old_max)

def low_bound(primes):
    ''' Find the lower bound for the number of consecutive integers '''
    total, end = 0, 0
    while total < 1000000:
        total += primes[end]
        end += 1
    if end % 2:
        end -= 1
    for x in range(end, 1, -2):
        cur_sum = sum(primes[0:x])
        if cur_sum in primes:
            return x, cur_sum
    return 0, None

def check_all(consec, primes):
    ''' Check sums of consecutive primes, using 'consec' as a minimum range '''
    cur_sum, cur_max, s = 0, 0, 0
    while sum(primes[s:s+consec]) < 1000000:
        x = 1
        s += 1
        cur_sum = 0
        while cur_sum < 1000000:
            cur_sum = sum(primes[s:s+consec+x])
            if cur_sum in primes:
                consec += x-1
                cur_max = cur_sum
            x += 2
    return consec, cur_max

if __name__ == "__main__":
    main()
