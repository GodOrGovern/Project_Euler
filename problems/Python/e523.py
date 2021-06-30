''' Consider the following algorithm for sorting a list:
    1. Starting from the beginning of the list, check each pair of adjacent
       elements in turn.
    2. If the elements are out of order:
        a. Move the smallest element of the pair at the beginning of the list.
        b. Restart the process from step 1.
    3. If all pairs are in order, stop.
Let F(L) be the number of times step 2a is executed to sort list L. Let E(n) be
the expected value of F(P) over all permutations P of the integers {1, 2, ...,
n}. Find E(30). Give your answer rounded to two digits after the decimal point '''

def main():
    ''' Driver function '''
    print(round(E(30), 2))

def E(n):
    ''' The average or expected number of times step 2a is executed in the
    sorting algorithm described in the prompt for a random permutation of the
    digits 1 to n '''
    return sum((2**(k-1)-1)/k for k in range(1, n+1))

def sort_steps(arr):
    ''' Returns the number of steps needed to sort the list 'arr'. I used this
    function to find the values of E(n) for n = 1 to 10 (sum across all
    permutations divided by number of permutations) the numerators of which I
    plugged into the OEIS to get the formula used to find E(30) '''
    high_val = 0
    steps = 0
    for i,n in enumerate(arr):
        high_val = max(n, high_val)
        # This is the crux of the piece. If the number n at index i is less
        # than at least one number before it (ie index less than i) it will
        # increase the number of step 2a executions by 2 to the power of the
        # number of values in arr before n in arr that are less than n
        if n != high_val:
            steps += 2**(sum(map(lambda n: n > x, arr[:i])))
    return steps

if __name__ == "__main__":
    main()
