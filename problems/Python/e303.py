''' For a positive integer n, define f(n) as the least positive multiple of n
that, written in base 10, uses only digits ≤ 2. Find ∑f(n)/n for n = 1 to
10000 '''

def main():
    ''' Driver function '''
    total = 0
    for n in range(1, 101):
        total += f(n) // n
    print(total)

def f(n):
    ''' Return the least positive multiple of 'n' that, written in base 10,
    uses only digits <= 2 '''
    cur = n
    while not {c for c in str(cur)}.issubset({'0', '1', '2'}):
        cur += n
    return cur

if __name__ == "__main__":
    main()