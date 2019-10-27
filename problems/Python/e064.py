''' How many continued fractions for N ≤ 10000 have an odd period? '''

from euler import periodic

def main():
    ''' Driver function '''
    count = 0
    for n in range(10000):
        if len(periodic(n)) % 2 == 1:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
