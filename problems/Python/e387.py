''' A Harshad number is a number that is divisible by the sum of its
digits. Let's call a Harshad number that, while recursively truncating the last
digit, always results in a Harshad number a right truncatable Harshad number.
Let's call a Harshad number that, when divided by the sum of its digits,
results in a prime a strong Harshad number. Take the number 2011 which is
prime. When we truncate the last digit from it we get 201, a strong Harshad
number that is also right truncatable. Let's call such primes strong, right
truncatable Harshad primes. Find the sum of the strong, right truncatable
Harshad primes less than 10**14 '''

from sympy import isprime

def main():
    ''' Driver function '''
    potential = right_trunc(10**14)
    potential = prime_div(potential)
    valid = make_prime(potential)
    print(sum(valid))

def right_trunc(end):
    ''' Return set of right truncatable Harshad numbers up to 'end' '''
    valid = {(n, n) for n in range(1, 10)}
    cur_group = valid
    next_group = set()
    cur, d_sum = cur_group.pop()
    while cur < end // 100:
        for n in range(10):
            pos = 10*cur+n
            if not pos % (d_sum+n):
                next_group.add((pos, d_sum+n))
        if not cur_group:
            cur_group = next_group
            next_group = set()
            valid.update(cur_group)
        cur, d_sum = cur_group.pop()
    return valid

def prime_div(nums):
    ''' Return the set numbers from 'nums' that yield a prime when divided
    by the sum of their digits '''
    valid = set()
    for n, d_sum in nums:
        if isprime(n // d_sum):
            valid.add(n)
    return valid

def make_prime(nums):
    ''' Return the set of numbers from 'nums' that can be made prime by
    appending a digit to the end '''
    valid = set()
    for n in nums:
        for x in [1, 3, 7, 9]:
            pos = 10*n+x
            if isprime(pos):
                valid.add(pos)
    return valid

if __name__ == "__main__":
    main()
