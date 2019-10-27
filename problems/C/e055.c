// How many Lychrel numbers are there below ten-thousand?

#include <stdio.h>
#include <stdbool.h>

bool isLychrel(long num, int count);
long reverseNum(long num);

int main(void)
{
    int count = 0;

    for (int i = 1; i < 10000; i++)
        if (isLychrel(i, 0))
            count += 1;

    printf("%i\n", count);
    return 0;
}

bool isLychrel(long num, int count)
{
    if (count > 50)
        return true;
    long reverse = reverseNum(num);
    if (reverse == num && count >= 1)
        return false;
    return isLychrel(num+reverse, count+1);
}

long reverseNum(long num)
{
    long reverse = 0;

    while (num > 0)
    {
        reverse = reverse * 10 + num % 10;
        num /= 10;
    }

    return reverse;
}
