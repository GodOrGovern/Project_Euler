''' Which starting number, under one million, produces the longest collatz
sequence? '''

def main():
    ''' Driver function '''
    print(longest_collatz(10**6))

def longest_collatz(end):
    ''' Return the number (less than end) that produces the longest Collatz
    sequence '''
    lengths = [0] * end
    for n in range(end-1, 1, -1):
        prev = [n]
        while n:
            if n < end and (lengths[n] != 0 or n == 1):
                for i,p in enumerate(prev[::-1]):
                    if p < end:
                        lengths[p] = lengths[n] + i + 1
                break
            n = (n // 2) if (n % 2 == 0) else (3*n + 1)
            prev.append(n)
    return lengths.index(max(lengths))

if __name__ == "__main__":
    main()
