''' Turan has the electrical water heating system outside his house in a shed.
The electrical system uses two fuses in series, one in the house and one in the
shed. (Nowadays old fashioned fuses are often replaced with reusable mini
circuit breakers, but Turan's system still uses old fashioned fuses.) For the
heating system to work both fuses must work. Turan has n fuses. He knows that m
of them are working and the rest are blown. However, he doesn't know which ones
are blown. So he tries different combinations until the heating system turns
on. We denote by T(m, m) the smallest number of tries required to ensure the
heating system turns on. Let L(N) be the sum of all T(N, m) for 2 <= m <= N.
Find L(10**7). '''

def main():
    ''' Driver function '''
    print(L(10**7))

def L(N):
    ''' Returns the value of L(N) (the function described in the problem) '''
    total = 0
    # Calculates the maximum tries required by the following strategy for all m:
    #   Split the fuses into m-1 groups of size n//(m-1) (n mod m-1 groups
    #   will have 1 extra). Within each group, test all fuses against each
    #   other. At least one group will have 2 working fuses, so the process
    #   will always find a successful pair.
    for m in range(2, N+1):
        group, remain = divmod(N, m-1)
        total += (m-1) * (group * (group - 1))//2 + group*remain
    return total

if __name__ == "__main__":
    main()
