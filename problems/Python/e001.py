''' Find the sum of all the multiples of 3 or 5 below 1000 '''

def main():
    ''' Driver function '''
    print(sum(n for n in range(1000) if not (n % 3 and n % 5)))

if __name__ == "__main__":
    main()