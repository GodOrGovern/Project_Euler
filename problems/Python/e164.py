''' How many 20 digit numbers n (without any leading zero) exist such that no
three consecutive digits of n have a sum greater than 9? '''

import numpy as np
from collections import defaultdict

def main():
    ''' Uses matrix multiplication to find the number of length-20 walks in
    'graph' '''
    triples = load_triples()
    graph = build_graph(triples)
    fst_matrix, matrix = build_matrices(triples, graph)
    orig_matrix = matrix
    matrix = np.matmul(fst_matrix, matrix)
    for _ in range(15):
        matrix = np.matmul(matrix, orig_matrix)
    print(int(sum(matrix.flat)))

def load_triples():
    ''' Return all permutations of triples that sum to 9 or less '''
    triples = []
    for x in range(10):
        for y in range(10):
            for z in range(10):
                triple = (x, y, z)
                if sum(triple) <= 9:
                    triples += [triple]
    return triples

def build_graph(triples):
    ''' Build a graph where the nodes are triples and the edges point from a
    node (with digits (a, b, c)) to another (with digits (b, c, d)) '''
    graph = defaultdict(list)
    for t1 in triples:
        for t2 in triples:
            if t1[1:] == t2[:2]:
                graph[t1] += [t2]
    return graph

def build_matrices(triples, graph):
    ''' Build two matrices where rows are origins and columns are endpoints. The
    value at 'matrix[i][j]' is the number of ways to get from 'i' to 'j'.
    'fst_matrix' only has triples where the first digit is not 0 in the from
    column. 'matrix' includes all triples '''
    triples_sort = sorted(triples)
    length = len(triples)
    fst_matrix = np.zeros((length, length), dtype=int)
    matrix = np.zeros((length, length), dtype=int)
    pos = dict()
    for i, t in enumerate(triples_sort):
        pos[t] = i
    for i, t1 in enumerate(triples_sort):
        for t2 in graph[t1]:
            if t1[0]:
                fst_matrix[i][pos[t2]] = 1
            matrix[i][pos[t2]] = 1
    return fst_matrix, matrix

if __name__ == "__main__":
    main()
