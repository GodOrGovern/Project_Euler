''' If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued, what is
the side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%? '''

from sympy.ntheory import isprime

def main():
    ''' Uses quadratic equations to find values along the diagonal of Ulam's
    spiral. One diagonal is ignored as it is solely squares of odd numbers '''
    prime, total = 8, 13
    while prime / total >= 0.10:
        x = (total + 3) // 4
        base = 4*x**2 + 1
        if isprime(base):
            prime += 1
        if isprime(base - 2*x):
            prime += 1
        if isprime(base + 2*x):
            prime += 1
        total += 4
    print((total + 1) // 2)

if __name__ == "__main__":
    main()
