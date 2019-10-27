''' Consider the isosceles triangle with base length, b=16, and legs, L=17.
Find ∑L for the twelve smallest isosceles triangles for which h=b±1 and b, L
are positive integers '''

from euler import convergent

def main():
    ''' This problem is reducible to the Pell equation k**2 - 5*L**2 = -1. The
    solutions to this equation can then be found by using the continued
    fraction expansion of sqrt(5). An additional constraint needed to be added
    as not all solutions to the Pell equation would necessarily be solutions to
    the overall problem '''
    count = 0
    nums = []
    for k, l in convergent(5, float("inf")):
        if k % 10 in {2, 3, 7, 8}:
            nums.append(l)
            count += 1
            if count == 12:
                break
    print(sum(nums))

if __name__ == "__main__":
    main()
