// Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0

#include <stdio.h>
#include <math.h>

int* findCoef(void);
int f(int a, int b);
int genPrime(int start);
int isPrime(int num);

int main(void)
{
    int *coef = findCoef();
    printf("%d\n", coef[0] * coef[1]);
    return 0;
}

int* findCoef(void)
{
    int maxPrime = 0;
    static int coef[2];
    for (int a=-999; a < 1000; a+=2)
    {
        int b = 2;
        while (b < 1000)
        {
            int curPrime = f(a, b);
            if (curPrime > maxPrime)
            {
                maxPrime = curPrime;
                coef[0] = a;
                coef[1] = b;
            }

            b = genPrime(b + 1);
        }
    }

    return coef;
}

int f(int a, int b)
{
    int n = 0;
    while (isPrime(n * (n + a) + b))
        n++;

    return n;
}

int genPrime(int start)
{
    return isPrime(start) ? start : genPrime(start+1);
}

int isPrime(int num)
{
    if (num < 0)
        return 0;

    for (int n=2; n < sqrt(num) + 1; n++)
        if (num % n == 0)
            return 0;

    return 1;
}
