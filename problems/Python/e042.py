''' By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. If the word
value is a triangle number then we shall call the word a triangle word.
How many are words in the source file are triangle words? '''

import csv
from euler import src_file

def main():
    ''' Driver function '''
    words = list(csv.reader(open(src_file('e042'))))[0]
    count = 0
    for word in words:
        value = word_value(word)
        if is_tri(value):
            count += 1
    print(count)

def word_value(word):
    ''' Get value of word based on alphabetical position of letters '''
    value = 0
    for letter in word:
        value += ord(letter) - 64
    return value

def is_tri(num):
    ''' Determine if num is a triangle number '''
    if (1 + 8*num)**0.5 % 2 == 1:
        return True
    return False

if __name__ == "__main__":
    main()
