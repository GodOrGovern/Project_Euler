''' Find the next triangle number that is also pentagonal and hexagonal. '''

from math import sqrt

def main():
    ''' Generates triangle numbers and checks if they are also pentagonal and
    hexagonal '''
    n = 286
    result = 0
    while not result:
        cur = n*(n+1)//2
        if is_pent(cur) and is_hex(cur):
            result = cur
        n += 1
    print(result)

def is_pent(n):
    ''' Determine if n is a pentagonal number '''
    if not (sqrt(1 + 24*n) - 5) % 6:
        return True
    return False

def is_hex(n):
    ''' Determine if n is a hexagonal number '''
    if not (sqrt(1 + 8*n) - 3) % 4:
        return True
    return False

if __name__ == "__main__":
    main()
