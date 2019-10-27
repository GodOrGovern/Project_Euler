''' Some positive integers n have the property that the sum n + reverse(n)
consists entirely of odd (decimal) digits. Leading zeroes are not allowed in
either n or reverse(n). How many reversible numbers are there below 10**9? '''

def main():
    ''' The answer for 10**8 is equivalent to the answer for 10**9 '''
    nums = {x for x in range(1, 10**8)}
    count = 0
    while nums:
        n = nums.pop()
        if not n % 10:
            continue
        n_rev = int(str(n)[::-1])
        if n_rev in nums:
            nums.remove(n_rev)
        if not n % 2 ^ n_rev % 2:
            continue
        count += odd_digits(n+n_rev) * 2
    print(count)

def odd_digits(n):
    ''' Determine if 'n' is comprised entirely of odd digits '''
    while n:
        if not n % 10 % 2:
            return False
        n //= 10
    return True

if __name__ == "__main__":
    main()
