''' Let r be the remainder when (a−1)**n + (a+1)**n is divided by a**2. For 3 ≤
a ≤ 1000, find ∑ r_max '''

def main():
    ''' Driver function '''
    total = 0
    for a in range(3, 1001):
        seen = set()
        a_sqr = a**2
        for n in range(1, 1001):
            seen.add((pow(a-1, n, a_sqr) + pow(a+1, n, a_sqr)) % a_sqr)
        total += max(seen)
    print(total)

if __name__ == "__main__":
    main()
