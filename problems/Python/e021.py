''' Let d(n) be defined as the sum of proper divisors of n. If d(a) = b and
d(b) = a, where a != b, then a and b are an amicable pair and each of a and b
are called amicable numbers. Evaluate the sum of all the amicable numbers
under 10000 '''

from sympy import divisors

def main():
    ''' Driver function '''
    nums = {n for n in range(2, 10000)}
    amicable = []
    while nums:
        num = nums.pop()
        div_sum = sum(divisors(num)[:-1])
        if num == sum(divisors(div_sum)[:-1]) and num != div_sum:
            amicable.append(num)
    print(sum(amicable))

if __name__ == "__main__":
    main()
