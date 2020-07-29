''' A spider, S, sits in one corner of a cuboid room and a fly, F, sits in
the opposite corner. There are up to three "shortest" path candidates for any
given cuboid and the shortest route doesn't always have integer length. Find
the least value of M such that the number of solutions first exceeds one
million '''

from euler import gen_triple

def main():
    ''' I manually binary searched by adjusting the 'end' variable '''
    end = 1818
    count = 0
    for t in gen_triple():
        if t.min() > end:
            continue
        t.sort()
        a, b = t[0], t[1]
        while a <= end and b <= 2*end:
            for n in range(b-1 if b <= end else end, b//2-(b+1)%2, -1):
                count += b-n <= n <= a
            if b <= end:
                for n in range(a-1, a//2-(a+1)%2, -1):
                    count += a-n <= n <= b
            a, b = a+t[0], b+t[1]
        print(count)

if __name__ == "__main__":
    main()
