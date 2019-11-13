''' Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares '''

from euler import get_palindromes

def main():
    ''' Driver function '''
    end = 10**8
    sqr_sums = square_sums(end)
    print(sum(sqr_sums.intersection(get_palindromes(1, end))))

def square_sums(end):
    ''' Returns a set of all possible sums of consecutive squares, which go up to 'end' '''
    sqrs = squares_to(end)
    cur_sqr_sum = sum(sqrs)
    sqr_sums = set()
    for i, n1 in enumerate(sqrs[:-1]):
        cur_sqr_sum = n1
        for n2 in sqrs[i+1:]:
            cur_sqr_sum += n2
            sqr_sums.add(cur_sqr_sum)
    return sqr_sums

def squares_to(end):
    ''' Returns a list of squares up to 'end' '''
    sqrs = []
    n = 1
    n_sqr = 1
    while n_sqr < end:
        sqrs.append(n_sqr)
        n_sqr += 2*n + 1
        n += 1
    return sqrs

if __name__ == "__main__":
    main()