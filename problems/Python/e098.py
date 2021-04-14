''' By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 362. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a
different letter have the same digital value as another letter. Using e098
which contains nearly two-thousand common English words, find all the square
anagram word pairs (a palindromic word is NOT considered to be an anagram of
itself). What is the largest square number formed by any member of such a
pair? '''

from collections import defaultdict
from itertools import permutations
from euler import src_file

def main():
    ''' Driver functions '''
    anagrams = get_anagrams(src_file('e098'))
    max_length = len(max(anagrams, key=lambda i: len(i[0]))[0])
    sqrs, sqr_set = squares_by_length(max_length)
    max_sqr = 0
    for a in anagrams:
        for w1, w2 in permutations(a, 2):
            for s in sqrs[len(a[0])]:
                valid = True
                vals = dict()
                nums = set()
                for i, c in enumerate(w1):
                    if (s[i] in nums and (c not in vals or s[i] != vals[c])) or (c in vals and s[i] != vals[c]):
                        valid = False
                        break
                    nums.add(s[i])
                    vals[c] = s[i]
                if valid:
                    new = ''.join(vals[c] for c in w2)
                    if new in sqr_set:
                        max_sqr = max(max(max_sqr, int(new)), int(s))
    print(max_sqr)

def get_anagrams(fName):
    ''' Return a list of lists where each sublist contains 2 or more words that
    are anagrams of each other '''
    ordered = defaultdict(list)
    for w in open(fName).read().replace('"', '').split(','):
        alpha = ''.join(sorted(w))
        ordered[alpha] += [w]
    return [v for v in ordered.values() if len(v) > 1]

def squares_by_length(longest):
    ''' Return a set of squares and a list of lists where each sublist contains
    all squares with a length equal to the index of the list. For example,
    'sqrs[4]' contains all squares of length 4. All values are strings '''
    sqr_set = set()
    sqrs = [[] for _ in range(longest+2)]
    sqr = n = 1
    while len(str(sqr)) <= longest:
        sqr = n**2
        sqr_set.add(str(sqr))
        sqrs[len(str(sqr))] += [str(sqr)]
        n += 1
    return sqrs, sqr_set

if __name__ == "__main__":
    main()
