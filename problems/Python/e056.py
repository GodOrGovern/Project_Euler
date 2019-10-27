''' Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum? '''

def main():
    ''' Brute-force all possibilities '''
    cur_max = 0
    for a in range(100):
        for b in range(100):
            cur_max = max(cur_max, sum([int(n) for n in str(a**b)]))
    print(cur_max)

if __name__ == "__main__":
    main()
