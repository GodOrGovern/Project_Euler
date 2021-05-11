''' Given is the function f(x) = floor(2**30.403243784-x*x) * 10**-9 the
sequence u_n is defined by u_0 = -1 and u_{n+1} = f(u_n). Find u_n + u_{n+1}
for n = 10**12. Give your answer with 9 digits after the decimal point.'''

from math import floor

def main():
    ''' Driver function '''
    # Function quickly converges and alternates between two values so the
    # sequence only needs to be generated up until about n = 1000
    f = lambda x: floor(2**(30.403243784-x*x)) * 10**(-9)
    u = -1
    for _ in range(1000):
        prev = u
        u = f(u)
    print(prev+u)

if __name__ == "__main__":
    main()
