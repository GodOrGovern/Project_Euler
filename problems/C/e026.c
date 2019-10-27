// Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#include <stdio.h>
#include <math.h>
#include "euler.h"

int genPrime(int start);
int isPrime(int num);

int main(void)
{
    int maxLength = 0;
    int denom = 7;
    while (denom < 1000)
    {
        if (multiOrder(10, denom) > maxLength)
            maxLength = denom;

        denom = genPrime(denom + 1);
    }

    printf("%d\n", maxLength);
    return 0;
}


int genPrime(int start)
{
    return isPrime(start) ? start : genPrime(start+1);
}

int isPrime(int num)
{
    if (num <= 3)
    {
        if (num <= 1)
            return 0;
        return 1;
    }

    if (!(num % 2 && num % 3))
        return 0;

    for (int n=2; n < sqrt(num) + 1; n++)
        if (num % n == 0)
            return 0;

    return 1;
}
