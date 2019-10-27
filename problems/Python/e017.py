''' If all the numbers from 1 to 1000 inclusive were written out in words, how
many letters would be used? '''

import inflect

def main():
    ''' Uses inflect engine to write out numbers '''
    engine = inflect.engine()
    letters = 0
    for n in range(1, 1001):
        num = engine.number_to_words(n)
        num = num.replace(' ', '')
        num = num.replace('-', '')
        letters += len(num)
    print(letters)

if __name__ == "__main__":
    main()
