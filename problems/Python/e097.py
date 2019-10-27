''' in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433*2**7830457+1. Find the last ten digits of this prime
number '''

def main():
    ''' Does not actually calculate 2**7830457, just the last ten digits '''
    last = 1
    for _ in range(1, 7830458):
        last = last * 2 % 10**10
    print(str(last*28433+1)[-10:])

if __name__ == "__main__":
    main()
