''' Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits '''

def main():
    ''' Driver function '''
    success = 0
    for x in range(10, 200000):
        if x == sum([int(n)**5 for n in str(x)]):
            success += x
    print(success)

if __name__ == "__main__":
    main()
