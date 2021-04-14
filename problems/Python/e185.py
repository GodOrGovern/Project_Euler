''' The game Number Mind is a variant of the well known game Master Mind.
Instead of coloured pegs, you have to guess a secret sequence of digits. After
each guess you're only told in how many places you've guessed the correct
digit. So, if the sequence was 1234 and you guessed 2036, you'd be told that
you have one correct digit; however, you would NOT be told that you also have
another digit in the wrong place '''

from euler import src_file

def main():
    ''' Driver function '''
    seqs = read_file(src_file('e185'))
    poss = poss_digits(seqs)
    def search(result, index):
        for val in seqs.values():
            if not (0 <= val <= (16-index)):
                return None
        if index == 16:
            for val in seqs.values():
                if val != 0:
                    return None
            return result
        for p in poss[index]:
            found = []
            for key in seqs.keys():
                if key[index] == p:
                    found += [key]
                    seqs[key] -= 1
            ans = search(result+[p], index+1)
            if ans:
                return ans
            for key in found:
                seqs[key] += 1
    print(''.join(str(n) for n in search([], 0)))

def read_file(file_name):
    ''' Load data from 'file_name' '''
    data = dict()
    with open(file_name) as f:
        for line in f:
            temp = line.split()
            data[tuple(int(c) for c in temp[0])] = int(temp[1])
    return data

def poss_digits(seqs):
    ''' Return a list of sets where each set contains the possible digits for
    that index '''
    seqs_sort = sorted(seqs, key=lambda n: seqs[n])
    poss = [set() for _ in range(16)]
    for s in seqs_sort[1:]:
        for i, n in enumerate(s):
            poss[i].add(n)
    for i, n in enumerate(seqs_sort[0]):
        if n in poss[i]:
            poss[i].remove(n)
    return poss

if __name__ == "__main__":
    main()
