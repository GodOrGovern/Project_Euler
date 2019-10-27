#include "euler.h"

long partition(int* parts, int partNum, int whole)
{
    long table[whole+1];
    memset(table, 0, sizeof(table));
    table[0] = 1;

    for (int i = 0; i < partNum; i++)
        for (int j = parts[i]; j <= whole; j++)
            table[j] += table[j - parts[i]];

    return table[whole];
}

// Calculate the sum of the digits in n, with func applied to each digit
long digitSum(long n, long (*func)(long))
{
    long sum = 0;
    do
        sum += (*func)(n%10);
    while (n /= 10);
    return sum;
}

// Find the multplicative order of 'a' modulo 'n'
int multiOrder(int a, long long n)
{
    int k = 1;
    int result = 1;
    while (k < n) {
        result = (result * a) % n;
        if (result == 1)
            return k;
        k++;
    }

    return -1;
}
