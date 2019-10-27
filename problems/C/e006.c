/* Find the difference between the sum of the squares of the first one hundred
   natural numbers and the square of the sum */

#include <stdio.h>
#include <math.h>

int main(void)
{
    int squareSum = 0;
    int sumSquare = 0;

    for (int i = 1; i <= 100; i++)
    {
        squareSum += i;
        sumSquare += pow(i, 2);
    }

    squareSum = pow(squareSum, 2);
    printf("%i\n", squareSum - sumSquare);
    return 0;
}