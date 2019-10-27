''' Given that L is the length of the wire, for how many values of L ≤
1,500,000 can exactly one integer sided right angle triangle be formed? '''

from euler import farey

def main():
    ''' Driver function '''
    vals = triple_perims(int(1.5e6))
    print(sum([x == 1 for x in vals.values()]))

def triple_perims(p):
    ''' All primitive Pythagorean triples are composed of coprime numbers that
    add to an odd number. Use a coprime generator to find the perimeters of
    primitive triples, which are used to calculate non-primitive perimeters.
    Return a dictionary with perimeters as keys and frequencies of keys as
    values '''
    values = dict()
    for a, b in farey(int(((1+2*p)**0.5-1)/2)+1):
        if not (a + b) % 2 or not a:
           continue
        prim_perim = 2*b*(b+a)
        perim = prim_perim
        while perim <= p:
            if perim in values:
                values[perim] += 1
            else:
                values[perim] = 1
            perim += prim_perim
    return values

if __name__ == "__main__":
    main()
