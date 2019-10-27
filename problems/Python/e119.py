''' The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 83 = 512. We shall define an to be the
nth term of this sequence and insist that a number must contain at least two
digits to have a sum. Find a_30. '''

from math import log

def main():
    ''' Driver function '''
    num = 10
    count = 0
    vals = set()
    for n in gen_powers():
        digi_sum = digit_sum(n)
        if digi_sum == 1 or n < 10:
            continue
        result = log(n, digi_sum)
        if n == digi_sum**round(result):
            vals.add(n)
            count = len(vals)
        if count == 30:
            break
    print(sorted(vals)[-1])

def gen_powers():
    ''' Generator of perfect powers. Generates all squares up to a certain
    number, followed by cubes, etc. The endpoint is then shifted up '''
    endpoint = 10**2
    powers = int(log(endpoint, 2))
    start = [2] * powers
    yield 1
    while True:
        power = 2
        while power < powers:
            num = start[power]
            val = num**power
            while val < endpoint:
                yield val
                num += 1
                val = num**power
            start[power] = num
            power += 1
        endpoint *= 10
        new_powers = int(log(endpoint, 2))
        start += [2] * (new_powers - powers)
        powers = new_powers

def digit_sum(n):
    ''' Return the sum of the digits of 'n' '''
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    main()
