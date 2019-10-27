''' We shall call a positive integer that is a repunit in at least two bases a
strong repunit. Find the sum of all strong repunits below 10**12 '''

def main():
    ''' Any given number n can be written as 11 in base n-1. Thus all numbers
    can be assumed to start at 1, meaning those that end up in 'count' can be
    represented as repunits in at least 2 different bases. This only works
    because repunit_in_base() yields numbers beginning at 111 (in base 'b') '''
    base = 2
    count = {1: 1}
    end = 10**12
    while base < end**0.5:
        for n in repunit_in_base(base):
            if n >= end:
                break
            count[n] = 1
        base += 1
    print(sum(count.keys()))

def repunit_in_base(b):
    ''' Generator for repunits in base b, starting at 111 '''
    exp = 2
    repunit = 1 + b**1
    while True:
        repunit += b**exp
        yield repunit
        exp += 1

if __name__ == "__main__":
    main()
