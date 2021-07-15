''' A bag contains one red disc and one blue disc. In a game of chance a player
takes a disc at random and its colour is noted. After each turn the disc is
returned to the bag, an extra red disc is added, and another disc is taken at
random. The player pays $1 to play and wins if they have taken more blue discs
than red discs at the end of the game. Find the maximum prize fund that should
be allocated to a single game in which fifteen turns are played. '''

from operator import mul
from math import factorial
from functools import reduce
from itertools import combinations

def main():
    ''' Driver function '''
    print(int(1 // prob_win(15)))

def prob_win(num_turns):
    ''' Determine the probability of winning the game described in the question
    where 'num_turns' is the number of turns taken '''
    total = 0
    nums = list(range(1, num_turns+1))
    for n in range((num_turns + 1) // 2):
        total += sum(reduce(mul, comb, 1) for comb in combinations(nums, n))
    return total / factorial(num_turns+1)

if __name__ == "__main__":
    main()
