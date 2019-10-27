''' 70 coloured balls are placed in an urn, 10 for each of the seven rainbow
colours. What is the expected number of distinct colours in 20 randomly picked
balls? Give your answer with nine digits after the decimal point '''

from sympy import binomial

def main():
    ''' Answer is equal to 7 * (1 - (60 choose 20) / (70 choose 20)) '''
    result = 7 * (1 - binomial(60, 20) / binomial(70, 20))
    print(result.evalf())

if __name__ == "__main__":
    main()
