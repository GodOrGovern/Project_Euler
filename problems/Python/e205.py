''' Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
3, 4. Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3,
4, 5, 6. Peter and Colin roll their dice and compare totals: the highest total
wins. The result is a draw if the totals are equal. What is the probability
that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven
decimal places in the form 0.abcdefg '''

from itertools import combinations_with_replacement as cwr

pete_comb = {(9,): 1, (1, 8): 9, (2, 7): 36, (3, 6): 84, (4, 5): 126,
             (1, 1, 7): 72, (1, 2, 6): 252, (1, 3, 5): 504, (1, 4, 4): 630,
             (2, 2, 5): 756, (2, 3, 4): 1260, (3, 3, 3): 1680,
             (1, 1, 1, 6): 504, (1, 1, 2, 5): 1512, (1, 1, 3, 4): 2520,
             (1, 2, 2, 4): 3780, (1, 2, 3, 3): 5040, (2, 2, 2, 3): 7560}

colin_comb = {(6,): 1, (1, 5): 6, (2, 4): 15, (3, 3): 20, (1, 1, 4): 30,
              (1, 2, 3): 60, (2, 2, 2): 90, (1, 1, 1, 3): 120,
              (1, 1, 2, 2): 180, (1, 1, 1, 1, 2): 360, (1, 1, 1, 1, 1, 1): 720}

def main():
    ''' Driver function '''
    pete = total_probs([1, 2, 3, 4], 9, pete_comb)
    colin = total_probs([1, 2, 3, 4, 5, 6], 6, colin_comb)
    pete_wins = colin_prob = 0
    for i, prob in enumerate(pete):
        pete_wins += prob * colin_prob
        colin_prob += colin[i]
    print(pete_wins)

def total_probs(base, count, comb):
    ''' Get the probability of rolling each possible total. Return it in a list
    where the index is the total and the value is the probability.  Indexes 0
    through 'count-1' will have a value of 0 '''
    perms = len(base)**count
    probs = [0] * 37
    for roll in cwr(base, count):
        values = tuple(roll.count(n) for n in set(roll))
        values = tuple(sorted(values))
        probs[sum(roll)] += comb[values] / perms
    return probs

if __name__ == "__main__":
    main()
