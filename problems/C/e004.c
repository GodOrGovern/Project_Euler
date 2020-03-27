// Find the largest palindrome made from the product of two 3-digit numbers

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPalindrome(int num);

int main(void)
{
    int curMax = 0;
    for (int i = 999; i > 99; i--)
        for (int j = i; j > 99; j--)
        {
            int p = i*j;
            if (p > curMax && isPalindrome(p))
                curMax = p;
        }

    printf("%i\n", curMax);
    return 0;
}

bool isPalindrome(int num)
{
    int left = pow(10, (int)log10(num));

    while (num)
    {
        if (num / left != num % 10)
            return false;
        num %= left;
        num /= 10;
        left /= 100;
    }

    return true;
}
