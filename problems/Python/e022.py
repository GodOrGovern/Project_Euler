''' Begin by sorting it intoalphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score. What is the total of all the name
scores in the file? '''

from euler import src_file

def main():
    ''' Calculate score of each name and add to 'name_score' '''
    with open(src_file('e022')) as data:
        names = data.readline().replace('"', '').split(',')
    names = sorted([[ord(c)-64 for c in name] for name in names])
    print(sum(sum(name)*(i+1) for i, name in enumerate(names)))

if __name__ == "__main__":
    main()
