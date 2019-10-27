 /* By listing the set of reduced proper fractions for d ≤ 1,000,000 in
ascending order of size, find the numerator of the fraction immediately to the
left of 3/7 */

#include <stdio.h>
#include <math.h>

// Driver function
int main(void)
{
    double base = 3.0 / 7.0;
    double minDiff = 1;
    int minNum = 0;

    for (int i = 3; i < 1e6; i++)
    {
        if (!(i % 7))
            continue;
        int num = i*base;
        double diff = fabs((double)num/(double)i - base);
        if (diff < minDiff)
        {
            minDiff = diff;
            minNum = num;
        }
    }

    printf("%i\n", minNum);
    return 0;
}
