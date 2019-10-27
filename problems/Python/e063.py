''' How many n-digit positive integers exist which are also an nth power? '''

def main():
    ''' Brute-force for powers up to 22 '''
    base, power, length = 1, 1, 1
    count = 0
    while power < 22:
        while length <= power:
            length = len(str(base**power))
            if length == power:
                count += 1
            base += 1
        base = 1
        power += 1
    print(count)

if __name__ == "__main__":
    main()
