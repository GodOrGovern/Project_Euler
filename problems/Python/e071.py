''' By listing the set of reduced proper fractions for d ≤ 1,000,000 in
ascending order of size, find the numerator of the fraction immediately to the
left of 3/7 '''

def main():
    ''' Finds value closest to 3/7 for all x in the range 3 to 10**6. Checks
    difference between value and 3/7 against current minimum difference. If
    this were to be generalized, num would have to be checked to verify if its
    in simplest form '''
    base = 3 / 7
    cur_min = [1, 0]
    for x in range(3, 10**6):
        if x % 7 == 0:
            continue
        num = int(x*base)
        diff = abs(num/x - base)
        if diff < cur_min[0]:
            cur_min = [diff, num]
    print(cur_min[1])

if __name__ == "__main__":
    main()
