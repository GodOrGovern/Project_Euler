''' How many different ways can the tiles in a row measuring fifty units in
length be replaced with blocks of length 2, 3, and 4 if lengths cannot be mixed
and at least one block must be used? '''

def main():
    ''' Driver function '''
    print(sum(count_configs(50, l) for l in [2, 3, 4]))

def count_configs(n, l):
    ''' Return the number of ways to fill n tiles with blocks (at least 1) of
    length l. Dynamic programming solution '''
    dp = [[0 for _ in range(n+1)] for _ in range(n//l+1)]
    dp[1] = [max(0, r-l+1) for r in range(n+1)]
    # number of blocks
    for b in range(n//l+1):
        # starting position of the first block
        for p in range(n-b*l+1):
            # remaining tiles (for remaining blocks)
            for r in range((b-1)*l, n-p-l+1):
                dp[b][n-p] += dp[b-1][r]
    return sum(d[n] for d in dp)

if __name__ == "__main__":
    main()
