// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#include <stdio.h>
#include <math.h>

int digitFifthSum(int num);

int main(void)
{
    int success = 0;
    for (int x=10; x < 1000000; x++)
        if (x == digitFifthSum(x))
            success += x;

    printf("%i\n", success);
    return 0;
}

int digitFifthSum(int num)
{
    int sum = 0;
    while (num != 0)
    {
        sum += pow(num % 10, 5);
        num /= 10;
    }

    return sum;
}
