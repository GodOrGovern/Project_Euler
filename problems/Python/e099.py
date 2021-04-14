''' Using the source file, which  contains one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest
numerical value '''

from math import log
from euler import src_file

def main():
    ''' Driver function '''
    pairs = load_data(src_file('e099'))
    cur_max = pairs[0]
    for p in pairs[1:]:
        exp = log(cur_max[0], p[0])
        if p[1] // exp >= cur_max[1]:
            cur_max = p
    print(pairs.index(cur_max) + 1)

def load_data(infile):
    ''' Loads base, exponent pairs from infile into a list of lists '''
    pairs = []
    with open(infile) as data:
        for line in data:
            vals = line.strip().split(',')
            pairs.append([int(x) for x in vals])
    return pairs

if __name__ == "__main__":
    main()
