''' The text file e096 contains fifty different Su Doku puzzles ranging in
difficulty, but all with unique solutions. By solving all fifty puzzles find
the sum of the 3-digit numbers found in the top left corner of each solution
grid '''

from euler import src_file
from sudoku import solve

def main():
    ''' Driver function '''
    total = 0
    for puzzle in load_puzzles(src_file('e096')):
        solved = solve(puzzle)
        total += int(solved['A1'] + solved['A2'] + solved['A3'])
    print(total)

def load_puzzles(f_name):
    ''' Generator that yields sudoku puzzles found in file represented by
    'f_name' as lists of lists '''
    with open(f_name) as data:
        for _ in range(50):
            puzzle = []
            data.readline()
            for _ in range(9):
                puzzle += [n for n in data.readline().strip()]
            yield puzzle

if __name__ == "__main__":
    main()
