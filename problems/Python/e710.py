''' We shall define a twopal to be a palindromic tuple having at least one
element with a value of 2. It should also be noted that elements are not
restricted to single digits. Let t(n) be the number of twopals whose elements
sum to n. Find the least value of n such that t(n) is divisible by one
million '''

def main():
    ''' This was of great help: https://math.stackexchange.com/q/2086703/.
    'cur' and 'prev' hold the two most recent values of t(n). 'g' holds the three
    currently relevant values of the recursive 'g' function described in the
    above link. Values of t(n) are generated iteratively until a value
    divisible by one million is found '''
    n = 6
    mod = 10**6
    cur, prev = 4, 2
    g = [1, 2, 4]
    while cur % mod:
        if n % 2 == 1:
            cur = prev - g[0]
            g = [g[1], g[2], (2*g[2]-g[1]+g[0]) % mod]
        else:
            cur = (prev + pow(2, (n-2)//2, mod) + g[1] - g[2]) % mod
            prev = cur
        n += 1
    print(n-1)

if __name__ == "__main__":
    main()
