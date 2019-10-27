// How many different ways can £2 be made using any number of coins?

#include <stdio.h>

#include "euler.h"

// Driver function
int main(void)
{
    int coins[] = {1, 2, 5, 10, 20, 50, 100, 200};
    long total = partition(coins, 8, 200);
    printf("%li\n", total);
    return 0;
}
