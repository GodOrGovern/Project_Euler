''' What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid found in the source
file? '''

import numpy as np
from euler import src

def main():
    ''' Driver function '''
    data = open(src+'e011', 'r')
    grid = load_grid(data)
    maximum = max([max_across(grid), max_across(np.rot90(grid)), max_diag(grid),
                   max_diag(np.fliplr(grid))])
    print(maximum)

def load_grid(data):
    ''' Load data into grid '''
    data.seek(0)
    grid = np.array([[int(n) for n in line.rstrip().split()] for line in data])
    return grid

def max_across(grid):
    ''' Return greatest product of four adjacent numbers across grid '''
    maximum = 1
    for row in grid:
        temp = [np.prod(p) for p in [row[y:y+4] for y in range(len(row) - 3)]]
        maximum = max(max(temp), maximum)
    return maximum

def max_diag(grid):
    ''' Return greatest product of four adjacent numbers diagonally across grid '''
    maximum = 1
    shape = grid.shape
    for diag in [grid.diagonal(n) for n in range(4 - shape[1], shape[0] - 3)]:
        temp = [np.prod(p) for p in [diag[x:x+4] for x in range(len(diag) - 3)]]
        maximum = max(max(temp), maximum)
    return maximum

if __name__ == "__main__":
    main()
