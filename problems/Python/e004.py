''' Find the largest palindrome made from the product of two 3-digit numbers '''

def main():
    ''' Generate all possible products of 3-digit numbers, keep track of
    largest palindrome '''
    cur_max = 0
    for n1 in range(999, 99, -1):
        for n2 in range(999, 99, -1):
            p = n1*n2
            if p < cur_max:
                continue
            if str(p) == str(p)[::-1]:
                cur_max = p
    print(cur_max)


if __name__ == "__main__":
    main()
