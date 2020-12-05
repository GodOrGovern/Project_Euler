''' Define s(n) to be the smallest number that has a digit sum of n. Let S(k) =
the sum of s(n) for k = 1 to n. Further let f(i) be the fibonacci sequence with
f(0) = 0 and f(1) = 1. Find the sum of S(f(i)) for i = 2 to 90. Give your
answer modulo 1000000007 '''

def main():
    ''' Driver function '''
    fib = [0, 1]
    for _ in range(89):
        fib += [fib[-1] + fib[-2]]
    mod = 1000000007
    print(sum(S(n, mod) for n in fib[2:]) % mod)

def S(n, mod):
    ''' Closed form expression for S(n) modulo 'mod'. To avoid unnecessary
    clutter, say f(n)=10**(n//9) and F(n)=sum of f(k) for k = 1 to n. s(n) is
    given by the expression f(n) + f(n)*(n%9) - 1. Thus S(n) can be described
    as the sum of three summations from k = 1 to n: f(k), f(k)*(k%9), and -1.
    The first summation is equal to F(n). Given that s(n) can also be expressed
    as s(n)=F(n)-f(n)+1, some re-arranging yields F(n)=s(n)+f(n)-1. The 2nd
    summation (call it g(n)) can also be directly computed given n,
    g(n)=f(n)*(4+((n%9)*((n%9)+1))//2)-4. Since writing out a full explanation
    for this expression would be tedious, it suffices to say that it can be
    derived by considering the sum of the first n integers. The last summation
    is clearly equal to -n. Putting it all together, we get
    S(n)=s(n)+g(n)+f(n)-n-1. As 10**(n//9) is the only term that may become too
    large, it helps to factor it out and use the identity a*b (mod c) = (a mod
    c) * (b mod c) (mod c)'''
    return (pow(10, n//9, mod)*(6 + (n%9) + ((n%9)*((n%9)+1)//2)) - n - 6) % mod

if __name__ == "__main__":
    main()
