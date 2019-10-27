''' Sam and Max are asked to transform two digital clocks into two "digital
root" clocks. A digital root clock is a digital clock that calculates digital
roots step by step. When a clock is fed a number, it will show it and then it
will start the calculation, showing all the intermediate values until it gets
to the result. The clocks consume energy only when segments are turned on/off.
Sam's clock turns off the whole panel between calculations. Max's clock works
differently. Instead of turning off the whole panel, it is smart enough to
turn off only those segments that won't be needed for the next number. The two
clocks are fed all the prime numbers between A = 10**7 and B = 2*10**7. Find
the difference between the total number of transitions needed by Sam's clock
and that needed by Max's one. '''

from bitarray import bitarray
from pyprimesieve import primes

def main():
    '''Indices of 'bitmasks' represent different light segments on a digital
    clock. If 0 is considered the most significant index then 0=bottom-left,
    1=top-left, 2=bottom-middle, 3=mid-middle, 4=top-middle, 5=bottom-right,
    6=top-right. Every digit in a number is converted into a 7-bit bitmask '''
    bitmask = {0: bitarray('1110111'), 1: bitarray('0000011'),
               2: bitarray('1011101'), 3: bitarray('0011111'),
               4: bitarray('0101011'), 5: bitarray('0111110'),
               6: bitarray('1111110'), 7: bitarray('0100111'),
               8: bitarray('1111111'), 9: bitarray('0111111')}
    sams, maxs = 0, 0
    for states in path_to_roots(bitmask):
        sams += sam_clock(states)
        maxs += max_clock(states)
    print(sams-maxs)

def path_to_roots(bitmask):
    ''' Generator of lists containing the values between 'p' and its digital
    root. Values are represented using 'bitmask' '''
    for p in primes(10**7, 2*10**7):
        cur = []
        while p > 9:
            digits = [int(n) for n in str(p)]
            cur += [[bitmask[d] for d in digits]]
            p = sum(digits)
        yield cur + [[bitmask[p]]]

def sam_clock(states):
    ''' Given a list of bitarrays defining how the clock will light up,
    calculate the total number of transitions for Sam's clock '''
    return 2*sum(sum(n.count() for n in s) for s in states)

def max_clock(states):
    ''' Given a list of bitarrays defining how the clock will light up,
    calculate the total number of transitions for Max's clock '''
    total = sum(n.count() for n in states[0])
    for i, s in enumerate(states[:-1]):
        total += sum(n.count() for n in get_xor(s, states[i+1]))
    return total + sum(n.count() for n in states[-1])

def get_xor(a, b):
    ''' Return the result of XORing each index of 'a' with the corresponding
    index of 'b'. If there is no corresponding index, append that index of 'a'
    to the result. Assumes 'a' is longer than 'b' '''
    diff = len(a) - len(b)
    return [n if i < diff else n ^ b[i-diff] for i, n in enumerate(a)]

if __name__ == "__main__":
    main()
