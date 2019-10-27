/* How many different ways can one hundred be written as a sum of at least two
positive integers? */

#include <stdio.h>

#include "euler.h"

// Driver function
int main(void)
{
    int valNum = 99;
    int vals[valNum];
    for (int i = 0; i < valNum; i++)
        vals[i] = i + 1;
    long total = partition(vals, valNum, 100);
    printf("%li\n", total);
    return 0;
}
