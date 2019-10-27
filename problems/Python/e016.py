''' What is the sum of the digits of the number 2**1000? '''

def main():
    ''' Driver function '''
    print(sum([int(x) for x in str(2**1000)]))

if __name__ == "__main__":
    main()
