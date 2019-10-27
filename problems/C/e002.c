/* By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms. */

#include <stdio.h>

#define MAX 4000000

void fib(int* curr, int* prev);

int main(void)
{
    long long total = 0;
    int prev = 1;
    int curr = 2;
    while (curr < MAX)
    {
        if (curr % 2 == 0)
            total += curr;

        fib(&curr, &prev);
    }

    printf("%lli\n", total);

    return 0;
}

void fib(int* curr, int* prev)
{
    int temp = *curr + *prev;
    *prev = *curr;
    *curr = temp;
}
