''' What is the value of the first triangle number to have over five hundred
divisors? '''

from sympy import divisor_count

def main():
    ''' Increases size of 'tri_num' until it has over 500 divisors '''
    tri_num, natural = 1, 1
    while divisor_count(tri_num) < 500:
        natural += 1
        tri_num += natural
    print(tri_num)

if __name__ == "__main__":
    main()
