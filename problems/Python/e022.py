''' Begin by sorting it intoalphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score. What is the total of all the name
scores in the file? '''

from euler import src

def main():
    ''' Calculate score of each name and add to 'name_score' '''
    with open(src+'e022') as data:
        names = data.readline().replace('"', '').split(',')
    for name in names:
        name = [ord(c) - 64 for c in name]
    names.sort()
    name_score = 0
    for index, name in enumerate(names):
        name_score += sum(name) * (index + 1)
    print(name_score)

if __name__ == "__main__":
    main()
