''' For any N, let f(N) be the last five digits before the trailing zeroes in
N!. Find f(1,000,000,000,000) '''

def main():
    ''' Driver function '''

def f(n):
    ''' Find the last five digits before the trailing zeroes in 'n!' '''
    cur = 1
    index = 2
    while n != 1:
        cur = trim_trail(cur*index) % 10**5
        index += 1
        if index == 10**5:
            index = 1
        n -= 1
    return cur

def trim_trail(n):
    ''' Trim the trailing zeroes off of 'n' '''
    while not n % 10:
        n //= 10
    return n

if __name__ == "__main__":
    main()
