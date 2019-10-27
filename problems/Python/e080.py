''' For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots. '''

from mpmath import sqrt, mp, mpf

def main():
    ''' Driver function '''
    total = 0
    mp.dps = 110
    for n in range(2, 100):
        if int(n**0.5)**2 == n:
            continue
        root = str(sqrt(n))
        root = root.replace('.', '')
        total += sum([int(x) for x in root[:100]])
    print(total)

if __name__ == "__main__":
    main()
