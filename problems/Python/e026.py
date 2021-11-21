''' Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part '''

from euler import mult_order

def main():
    ''' Make n coprime to 10 and then check the order of 10 modulo n '''
    max_n = 0
    max_length = 0
    for n in range(3, 1000, 2):
        coprime_n = n
        while coprime_n % 2 == 0:
            coprime_n //= 2
        while coprime_n % 5 == 0:
            coprime_n //= 5
        cur_length = mult_order(10, coprime_n)
        if cur_length > max_length:
            max_n = n
            max_length = cur_length
    print(max_n)

if __name__ == "__main__":
    main()
