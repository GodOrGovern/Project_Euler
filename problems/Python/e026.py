''' Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part '''

from sympy.ntheory import n_order

def main():
    ''' Make n coprime to 10 and then check the order of 10 modulo n '''
    max_length = 0
    for n in range(3, 1000, 2):
        while n % 2 == 0:
            n //= 2
        while n % 5 == 0:
            n //= 5
        max_length = max(n_order(10, n), max_length)
    print(max_length)

if __name__ == "__main__":
    main()
