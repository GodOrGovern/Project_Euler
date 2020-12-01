''' Define p(L,n) to be the nth-smallest value of j such that the base 10
representation of 2**j begins with the digits of L. Find p(123,678910) '''


def main():
    ''' Integers 'n' such that the first three digits of 2^n equal 123 are
    separated by 196, 289, or 485 '''
    cur = 90
    count = 1
    while count < 678910:
        for n in [cur+196, cur+289, cur+485]:
            if log10(1.23) <= (n*log10(2) - int(n*log10(2))) <= log10(1.24):
                cur = n
                break
        count += 1
    print(cur)

if __name__ == "__main__":
    main()
