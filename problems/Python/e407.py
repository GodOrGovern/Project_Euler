''' Let's call M(n) the largest value of a < n such that a**2 ≡ a (mod n). Find
∑M(n) for 1 ≤ n ≤ 10**7 '''

from pyprimesieve import primes, factorize

def main():
    ''' Driver function '''
    end = 10**5
    total = idempotents_sum(end)
    print(total)

def idempotents_sum(end):
    ''' Find the largest idempotent of 'a' mod 'n' for all 'n' in the range 2
    to 'end'. Return the sum of the idempotents '''
    total = 0
    powers = prime_powers(end)
    idempotents = prime_power_idempotents(end, powers)
    for n in range(2, end+1):
        if n in powers:
            total += 1
            continue
        factors = factorize(n)
        first = factors[0][0]**factors[0][1]
        second = factors[1][0]**factors[1][1]
        common = idempotents[first].intersection(idempotents[second])
        for p, e in factors[2:]:
            common.intersection_update(idempotents[p**e])
        total += (1-min(common)) % n
    return total

def prime_power_idempotents(end, powers):
    ''' For each prime power, generate all numbers up to end for which 'n % p'
    is 0 or 1 (natural 'n' and prime power 'p'). Return as dict of sets '''
    nums = dict()
    for p in powers:
        cur = p
        cur_set = set()
        while cur < end:
            cur_set.update({cur, cur+1})
            cur += p
        nums[p] = cur_set
    return nums

def prime_powers(end):
    ''' Return set of all primes raised to an increasing power 'n' until the
    result is greater than 'end' '''
    powers = set()
    for p in primes(end):
        cur = p
        while cur <= end:
            powers.add(cur)
            cur *= p
    return powers

if __name__ == "__main__":
    main()
