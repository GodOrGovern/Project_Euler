''' By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms '''

from euler import fib

def main():
    ''' Driver function '''
    total = 0
    end = 4 * 10**6
    for f in fib():
        if not f % 2:
            total += f
        if f > end:
            break
    print(total)

if __name__ == "__main__":
    main()
