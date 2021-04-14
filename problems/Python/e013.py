''' Work out the first ten digits of the sum of the one-hundred
50-digit numbers found in the source file '''

from euler import src_file

def main():
    ''' Sums the numbers and finds the first 10 digits '''
    with open(src_file('e013')) as data:
        num = sum(int(line.strip()) for line in data)
    print(str(num)[:10])

if __name__ == "__main__":
    main()
