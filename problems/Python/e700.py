''' Consider the sequence 1504170715041707n mod 4503599627370517. An element of
this sequence is defined to be an Eulercoin if it is strictly smaller than all
previously found Eulercoins. Find the sum of all Eulercoins. '''

def main():
    ''' Driver function '''
    a, b = 1504170715041707, 4503599627370517
    print(sum(get_coins(a, b, 10**8)))

def get_coins(a, b, stop):
    ''' Return a sorted list of coins from the sequence a*n mod b. At first
    coins are found by repeatedly increasing n and keeping track of the lowest
    values produced. Once a coin falls below a certain threshold ('stop'),
    n is calculated for all values of a*n % b from 1 to the last coin found. If
    a given n is lower than every other n encountered thus far, excluding coins
    found using the first method, a*n % b must be a coin. '''
    cur = a % b
    coins = [cur]
    while cur > stop:
        cur = (a + cur) % b
        if cur < coins[-1]:
            coins += [cur]
    low = float("inf")
    x, _ = xgcd(a, b)
    for c in range(1, cur):
        n = c*x % b
        if n < low:
            low = n
            coins += [c]
    return sorted(coins)

def xgcd(a, b):
    ''' Extended Euclidean algorithm. Return x and y such that a*x + b*y =
    gcd(a, b) '''
    px, py = 1, 0
    x, y = 0, 1
    while b:
        q, r = divmod(a, b)
        x, px = px - q*x, x
        y, py = py - q*y, y
        a, b = b, r
    return px, py

if __name__ == "__main__":
    main()
