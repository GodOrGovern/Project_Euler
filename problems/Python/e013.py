''' Work out the first ten digits of the sum of the one-hundred
50-digit numbers found in the source file '''

from euler import src

def main():
    ''' Sums the numbers and finds the first 10 digits '''
    with open(src+'e013') as data:
        num = [line.rstrip() for line in data]
    num = ''.join(num)
    num = [int(num[n:n+50]) for n in range(len(num), 50)]
    print(str(sum(num))[:10])

if __name__ == "__main__":
    main()
