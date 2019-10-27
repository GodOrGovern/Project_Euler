''' There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc '''

from euler import gen_triple

def main():
    ''' Driver function '''
    print(test_triples().prod())

def test_triples():
    ''' Test primitive Pythagorean triples (and by extension, their
    non-primitive descendants) until one is found that constitutes a
    triangle with a perimeter of 1000 '''
    for triple in gen_triple():
        perimeter = triple.sum()
        if 1000 % perimeter == 0:
            return triple*1000//perimeter

if __name__ == "__main__":
    main()
