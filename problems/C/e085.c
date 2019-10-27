/* By counting carefully it can be seen that a rectangular grid measuring 3 by
2 contains eighteen rectangles. Although there exists no rectangular grid that
contains exactly two million rectangles, find the area of the grid with the
nearest solution. */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int allMin(void);
int* mMin(int m);

int main(void)
{
    printf("%i\n", allMin());
    return 0;
}

int allMin(void)
{
    int minDist = 2e6;
    int vals[2];
    int* temp;
    int m = 1;
    do
    {
        free(temp);
        temp = mMin(m);

        if (temp[1] < minDist)
        {
            minDist = temp[1];
            vals[0] = m, vals[1] = temp[0];
        }

        m++;
    }
    while (temp[0] >= m);

    free(temp);
    return vals[0]*vals[1];
}

int* mMin(int m)
{
    int prev = 0, cur = 0, n = 0;
    while (cur >= 0)
    {
        prev = cur;
        cur = 2e6 - m*n*(m+1)*(n+1)/4;
        n++;
    }

    int* temp = (int*)malloc(sizeof(int)*2);
    temp[0] = n-1;
    temp[1] = prev;
    if (prev + cur > 0)
        temp[1] = -1*cur;
    else
        temp[0] -= 1;
    return temp;
}
