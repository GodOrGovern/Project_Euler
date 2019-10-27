''' For which value of p ≤ 1000, is the number of solutions maximised? '''

from math import gcd

def main():
    ''' Find perimeters of pythagorean triples. Uses a formula to generate
    primitive triples and expands upon them '''
    success = []
    for x in range(1, 500):
        for y in filter(lambda y: gcd(x, y) == 1, range(x, 1000-x)):
            prim_per = 2*x*(x + y)
            non_prim = prim_per
            while non_prim < 1000:
                success.append(non_prim)
                non_prim += prim_per
    print(max(set(success), key=success.count))

if __name__ == "__main__":
    main()
