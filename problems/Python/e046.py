''' What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square? '''

from sympy.ntheory import isprime

def main():
    ''' Driver function '''
    n = 9
    while not goldbach(n):
        n += 2
        while isprime(n):
            n += 2
    print(n)

def goldbach(n):
    ''' Return True if n fails to meets the conditions of Goldbach's
    conjecture '''
    s = 0
    p = n
    while p >= 2:
        p = n - 2*s**2
        s += 1
        if isprime(p):
            return False
    return True

if __name__ == "__main__":
    main()
