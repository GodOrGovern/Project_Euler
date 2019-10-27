''' Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e '''

def main():
    ''' Driver function '''
    result = e_convergent(100)
    print(sum([int(n) for n in str(result)]))

def e_convergent(n):
    ''' Find the numerator of the nth convergent of e '''
    a = [1, 2, 1]
    num = [2, 2, 1]
    count = 1
    while count < n:
        index = (count-1) % 3
        num[0] = a[index]*num[1] + num[2]
        num[2], num[1] = num[1], num[0]
        if index == 1:
            a[index] += 2
        count += 1
    return num[0]

if __name__ == "__main__":
    main()
