''' Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit. '''

def main():
    ''' The original number has some restraints on which digits can go in
    each value place: the ones place must be a 0 and the tens place must be a 3
    or 7. This information can be used to narrow down the pool of potential
    candidates to 2 numbers per every 100 '''
    n1 = 10**9 + 30
    n2 = n1 + 40
    pattern = '1234567890'
    while n1 <= int(10**9 * 2**0.5):
        if str(n1**2)[::2] == pattern:
            print(n1)
            break
        if str(n2**2)[::2] == pattern:
            print(n2)
            break
        n1 += 100
        n2 += 100

if __name__ == "__main__":
    main()
