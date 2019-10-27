#ifndef EULER_H_
#define EULER_H_

#include <string.h>

// Calculate the number of ways whole can be partitioned using parts
long partition(int* parts, int partNum, int whole);
// Calculate the sum of the digits in n, with func applied to each digit
long digitSum(long n, long (*func)(long));
// Find the multplicative order of 'a' modulo 'n'
int multiOrder(int a, long long n);

#endif
