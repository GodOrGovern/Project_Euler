// What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#include <stdio.h>

int main(void)
{
    int start = 1;
    int length = 2;
    int total = 1;

    while (length + 1 <= 1001)
    {
        for (int n=1; n < 5; n++)
            total += start + length*n;

        start += length*4;
        length += 2;
    }

    printf("%i\n", total);
    return 0;
}
