''' Let f_n(k) = e^(k/n) - 1, for all non-negative integers k. Let g(n) = a^2 +
b^2 + c^2 + d^2 for a, b, c, d that minimize the error: |f_n(a) + f_n(b) +
f_n(c) + f_n(d) - π|. Find g(10000) '''

from math import e, pi, log

def main():
    ''' This will eventually work, it just might take until the heat death of
    the universe (at least for n=10000). Suggestions for future me: genetic
    algorithms, knapsack problem, subset sums '''
    target = pi
    n = 600
    f_inv = lambda x: int(n*log(x+1))
    f = [e**(k / n) - 1 for k in range(0, f_inv(pi))]
    quad = (0, 0, 0, 0)
    mindiff = float("inf")
    for a in range(f_inv(pi/4), f_inv(pi)):
        target = pi - f[a]
        for b in range(f_inv(target/3), min(a, f_inv(target))):
            target = pi - f[a] - f[b]
            for c in range(f_inv(target/2), min(b, f_inv(target))):
                target = pi - f[a] - f[b] - f[c]
                d = f_inv(target)
                target = abs(target - f[d])
                if target < mindiff:
                    mindiff = target
                    quad = (a, b, c, d)
    a, b, c, d = quad
    print(a**2 + b**2 + c**2 + d**2)

if __name__ == "__main__":
    main()
