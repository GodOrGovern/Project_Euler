''' Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000. '''

def main():
    ''' There's probably a better way to do this '''
    total = 0
    for x in range(1, 1001):
        total += x**x
    print(total % 10**10)

if __name__ == "__main__":
    main()
