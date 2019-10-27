/* A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before. What is most
amazing is that EVERY starting number will eventually arrive at 1 or 89. How
many starting numbers below ten million will arrive at 89? */

#include <stdio.h>

#include "euler.h"

int chain(long n);
long square(long n);

int main(void)
{
    int total = 0;
    for (int i = 1; i < 1e7; i++)
        total += chain(i);
    printf("%i\n", total);
    return 0;
}

int chain(long n)
{
    if (n == 1)
        return 0;
    if (n == 89)
        return 1;
    return chain(digitSum(n, square));
}

long square(long n) { return n*n; }
