''' How many hands in the source file does Player 1 win? '''

from collections import Counter
from euler import src_file

def main():
    ''' Driver function '''
    count = 0
    for line in open(src_file('e054')):
        p1 = line[0:14].split()
        p2 = line[15:29].split()
        if hand_rank(p1) > hand_rank(p2):
            count += 1
    print(count)

def hand_rank(hand):
    ''' Return value indicating rank of hand '''
    ranks = ['..23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    ranks, counts = list(zip(*Counter(ranks).most_common()))
    straight = len(ranks) == 5 and ranks[0]-ranks[-1] == 4
    flush = len({s for r, s in hand}) == 1
    count_rank = {(5,):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
                  (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}
    return max(count_rank[counts], 5*flush + 4*straight), ranks

if __name__ == "__main__":
    main()
