// What is the 10001st prime number?

#include <stdio.h>
#include <primesieve.h>

int main(void)
{
    printf("%li\n", primesieve_nth_prime(10001, 0));
    return 0;
}