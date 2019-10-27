/* Let s(n) be the smallest number m such that n divides m!. Let S(n) be
∑s(i) for 2 ≤ i ≤ n. Find S(10**8) */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int primePower(int p, int e);
long decomposition(int limit);
long sumArr(int* arr, int start, int end);
int* growArr(int* arr, int size);
int max(int a, int b);

// Complete ripoff (aka port) of https://bit.ly/2J9ByKf
int main(void)
{
    int limit = (int) pow(10, 8);
    printf("%li\n", decomposition(limit));
}

int primePower(int p, int e)
{
    int k = 0;
    while (e > p) {
        k += p;
        e -= p + 1;
        for (int i = k; (i /= p) % p == 0;) {
           e -= 1;
        }
    }

    return (k + max(0, e)) * p;
}

long decomposition(int limit)
{
    int primeLimit = (int)sqrt(limit);
    int primeSize = 100;
    int primeNumber = 0;
    int* primes = (int*)malloc(sizeof(int)*primeSize);
    int* s = (int*)malloc(sizeof(int)*(limit+1));
    memset(s, 0, (limit+1)*sizeof(int));
    int m = 2;

    for (int half = limit / 2; m <= half; m++) {
        if (!(s[m])) {
            s[m] = m;
            if (m <= primeLimit) {
                if (primeNumber == primeSize) {
                    primes = growArr(primes, (primeSize+=100)*sizeof(int));
                }
                primes[primeNumber] = m;
                primeNumber += 1;
            }
        }

        int s_m = s[m];
        int threshold = limit / m;
        for (int i = 0; i < primeNumber; i++) {
            int p = primes[i];
            if (p > threshold) {
                break;
            }
            if (m % p) {
                s[p * m] = s_m;
            }
            else {
                int e = 2;
                int q = m;
                while (!((q /= p) % p)) {
                    e += 1;
                }
                s[p * m] = max(primePower(p, e), s[q]);
            }
        }
    }

    for (int i = 0; i <= limit; i++) {
        if (!(s[i])) {
            s[i] = i;
        }
    }

    return sumArr(s, 2, limit);
}

int* growArr(int* arr, int size)
{
    int* newArr = (int*)realloc(arr, size);
    if (newArr == NULL) {
        printf("Could not allocate additional memory\n");
        exit(1);
    }
    return newArr;
}

long sumArr(int* arr, int start, int end)
{
    long total = 0;
    for (long i = start; i <= end; i++) {
        total += arr[i];
    }
    return total;
}

int max(int a, int b)
{
    return (a > b) ? a : b;
}
