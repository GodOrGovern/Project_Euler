''' The source file contains one thousand numbers written in valid, but not
necessarily minimal, Roman numerals. Find the number of characters saved by
writing each of these in their minimal form '''

from euler import src

def main():
    ''' Driver function '''
    total = 0
    with open(src+'e089') as data:
        for line in data:
            old_numeral = line.strip()
            num = roman_to_int(old_numeral)
            new_numeral = int_to_roman(num)
            total += len(old_numeral) - len(new_numeral)
    print(total)

def int_to_roman(num):
    ''' Convert integer 'num' to a Roman numeral '''
    numeral = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    for n, r in numeral.items():
        count = num // n
        result += r * count
        num -= n * count
    return result

def roman_to_int(roman):
    ''' Convert Roman numeral 'roman' to an integer '''
    total = 0
    numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i, n in enumerate(roman):
        add = (i+1 == len(roman)) or (numeral[roman[i+1]] <= numeral[n])
        total += numeral[n] if add else -numeral[n]
    return total

if __name__ == "__main__":
    main()
