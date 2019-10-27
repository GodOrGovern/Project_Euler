// Find the sum of all the multiples of 3 or 5 below 1000

#include <stdio.h>

int main(void)
{
    int total = 0;
    for (int i = 1; i < 1000; i++)
        if (!(i%3 && i%5))
            total += i;

    printf("%i\n", total);
    return 0;
}