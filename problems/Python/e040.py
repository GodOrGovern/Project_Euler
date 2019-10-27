''' If dn represents the nth digit of the fractional part, find the value of
the following expression:  d1 × d10 × d100 × d1000 × d10000 × d100000 ×
d1000000 '''

from math import log10, floor

def main():
    ''' Uses the range of possible indexes to calculate the relative location
    of index, which is then used to find the entire number in which index
    belongs. Lastly, the correct place value in this number is determined and
    the number in Champernowne's constant referenced by index is extracted '''
    result = 1
    for x in range(7):
        index = 10**x
        digits = get_digits(index)
        low, high = get_range(digits)
        mult = (index - low) / (high - low)
        num_range = 9 * 10**(digits-1)
        num = 10**(digits-1) + floor(num_range*mult)
        place_val = (index - low) % digits
        place_val = digits - place_val - 1
        result *= num // 10**place_val % 10
    print(result)

def get_digits(index):
    ''' Given the index of Champernowne's constant, return the number of digits in the
    number it corresponds to '''
    digits = floor(log10(index)) + 1
    check, _ = get_range(digits)
    if index >= check:
        return digits
    return digits - 1

def get_range(digits):
    ''' Given the number of digits, return the range of possible indexes in
    Champernowne's constant '''
    low_bound = 10**(digits-1) * (9*(digits-1) - 1) + 1
    low_bound //= 9
    up_bound = low_bound + 9*digits * 10**(digits-1)
    return low_bound + 1, up_bound

if __name__ == "__main__":
    main()
