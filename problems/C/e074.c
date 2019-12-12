/* 
 * Starting with 69 produces a chain of five non-repeating terms, but the
 * longest non-repeating chain with a starting number below one million is sixty
 * terms. How many chains, with a starting number below one million, contain
 * exactly sixty non-repeating terms? *
 */

#include <stdio.h>
#include <stdbool.h>

#include "euler.h"

int cycle(long cur, long* chain, int count);
bool nInArray(long n, long* array, int length);
long factorial(long n);

// Find cycle length for all values between 1 and 1e6
int main(void)
{
    long chain[60];
    int count = 0;

    for (int i = 0; i < 1e6; i++)
        if (cycle(i, chain, 0) == 60)
            count += 1;

    printf("%i\n", count);
    return 0;
}

// Find length of digit factorial cycles
int cycle(long cur, long* chain, int count)
{
    if (nInArray(cur, chain, count))
        return count;
    chain[count] = cur;
    return cycle(digitSum(cur, factorial), chain, count+1);
}

// Check if n is in first length elements of array
bool nInArray(long n, long* array, int length)
{
    for (int i = 0; i < length; i++)
        if (n == array[i])
            return true;
    return false;
}

// Find the factorial of n
long factorial(long n)
{
    long result = 1;

    while (n > 0)
    {
        result *= n;
        n--;
    }

    return result;
}
