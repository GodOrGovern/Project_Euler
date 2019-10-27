// What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

#include <stdio.h>
#include <gmp.h>

void fib(mpz_t a, mpz_t b, mpz_t c);

int main(void)
{
    mpz_t a, b, c;
    mpz_init_set_ui(a, 1);
    mpz_init_set_ui(b, 1);
    mpz_init(c);

    int index = 3;

    while (mpz_sizeinbase(c, 10) < 1000)
    {
        fib(a, b, c);
        index++;
    }

    printf("%i\n", index);
    return 0;
}

void fib(mpz_t a, mpz_t b, mpz_t c)
{
    mpz_add(c, a, b);
    mpz_set(a, b);
    mpz_set(b, c);
}
