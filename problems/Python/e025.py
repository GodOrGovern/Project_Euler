''' What is the index of the first term in the Fibonacci sequence to contain
1000 digits '''

from euler import fib

def main():
    ''' Driver function '''
    index = 1
    for f in fib():
        if len(str(f)) == 1000:
            break
        index += 1
    print(index)

if __name__ == "__main__":
    main()
