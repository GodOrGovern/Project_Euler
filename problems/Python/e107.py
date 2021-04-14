''' Using e107, a file containing a network with forty vertices, and given in
matrix form, find the maximum saving which can be achieved by removing
redundant edges whilst ensuring that the network remains connected. '''

from euler import src_file

def main():
    ''' Driver function '''
    matrix = load_matrix(src_file('e107'))
    init_weight = sum(sum(n for n in row if n != float("inf")) for row in matrix) // 2
    min_matrix = minimize_matrix(matrix)
    min_weight = sum(sum(n for n in row if n != float("inf")) for row in min_matrix) // 2
    print(init_weight - min_weight)

def minimize_matrix(matrix):
    ''' Return a new matrix that removes the most weight from matrix while
    keeping all nodes connected '''
    groups = []
    found = set()
    new_matrix = [[float("inf") for _ in row] for row in matrix]
    # Keep lowest weight edge for each node
    for i, row in enumerate(matrix):
        if i in found:
            continue
        min_node = row.index(min(row))
        new_matrix[min_node][i] = new_matrix[i][min_node] = matrix[i][min_node]
        found.update({i, min_node})
        for j, group in enumerate(groups):
            if min_node in group:
                groups[j].add(i)
                break
        else:
            groups += [{i, min_node}]
    # Keep minimal connection between each group of isolated nodes
    while len(groups) > 1:
        min1, min2 = 0, 0
        for n1 in groups[0]:
            for i, group in enumerate(groups[1:]):
                for n2 in group:
                    if matrix[n1][n2] < matrix[min1][min2]:
                        min1, min2 = n1, n2
                        min_group = i+1
        new_matrix[min1][min2] = new_matrix[min2][min1] = matrix[min1][min2]
        groups = [groups[0]|groups[min_group]] + groups[1:min_group] + groups[min_group+1:]
    return new_matrix

def load_matrix(file_path):
    ''' Return the matrix located at file_path as a list of lists, with empty
    cells (indicating no edge between nodes) represented as infinity. Each line
    corresponds to a row in the matrix with columns separated by commas '''
    matrix = []
    with open(file_path) as f:
        for i, line in enumerate(f):
            matrix += [[]]
            for val in line.strip().split(','):
                matrix[i] += [int(val)] if val != '-' else [float("inf")]
    return matrix

if __name__ == "__main__":
    main()
