''' Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2. For 3 ≤
a ≤ 1000, find ∑r_max '''

def main():
    ''' Brute-force '''
    total = 0
    for a in range(3, 1001):
        r_max = 0
        for n in range(1, a*2):
            r_max = max(r_max, (pow(a-1, n, a*a) + pow(a+1, n, a*a)) % (a*a))
        total += r_max
    print(total)

if __name__ == "__main__":
    main()
