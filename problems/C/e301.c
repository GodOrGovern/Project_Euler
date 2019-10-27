/* Nim is a game played with heaps of stones, where two players take it in turn
to remove any number of stones from any heap until no stones remain. We'll
consider the three-heap normal-play version of Nim, which works as follows: At
the start of the game there are three heaps of stones. On his turn the player
removes any positive number of stones from any single heap. The first player
unable to move (because no stones remain) loses. If (n1,n2,n3) indicates a Nim
position consisting of heaps of size n1, n2 and n3 then there is a simple
function X(n1,n2,n3) that returns: zero if, with perfect strategy, the player
about to move will eventually lose; or non-zero if, with perfect strategy, the
player about to move will eventually win. For how many positive integers
n ≤ 2**30 does X(n,2n,3n) = 0 ? */

#include <stdio.h>

/* If the result of XORing the three heaps is zero, the current player cannot
win assuming perfect play */
int main(void)
{
    int count = 0;
    for (int i = 0; i < (1 << 30); i++)
        count += (!(i ^ 2*i ^ 3*i));
    printf("%i\n", count);
    return 0;
}
