''' Tools that are useful for Project Euler '''

import numpy as np
from collections import defaultdict
from itertools import count

src = "/home/david/Documents/Programs/euler/problems/src/"

def get_palindromes(low, high):
    ''' Return a set of all palindromes in interval ['low', 'high'] '''
    def gen_palindrome():
        ''' Generator for palindromes, starting with 0 '''
        yield 0
        for digits in count(1):
            first = 10 ** ((digits - 1) // 2)
            for s in map(str, range(first, 10 * first)):
                yield int(s + s[-(digits % 2)-1::-1])
    palindromes = set()
    for p in gen_palindrome():
        if p > high:
            break
        if p < low:
            continue
        palindromes.add(p)
    return palindromes

def build_graph(infile, up=False, left=False):
    ''' Load graph into dictionary where edges are weighted. Default is to
    connect a given node to the nodes below and to the right of it. If up is
    set to True, the node above it will be connected. If left is set to true,
    the node to the left of it will be connected. '''
    graph = defaultdict(dict)
    matrix = []
    with open(infile) as data:
        matrix = [r.strip().split(',') for r in data.readlines()]
        height, width = len(matrix), len(matrix[0])
        for i1, r in enumerate(matrix):
            for i2, _ in enumerate(r):
                if 0 < i1 and up:
                    graph[(i1, i2)][(i1-1, i2)] = int(matrix[i1-1][i2])
                if i1 < height-1:
                    graph[(i1, i2)][(i1+1, i2)] = int(matrix[i1+1][i2])
                if 0 < i2 and left:
                    graph[(i1, i2)][(i1, i2-1)] = int(r[i2-1])
                if i2 < width-1:
                    graph[(i1, i2)][(i1, i2+1)] = int(r[i2+1])
        graph[(height-1,width-1)]
    return graph, matrix

def dijkstra(graph, start, end, dist=dict(), col=False):
    ''' Implementation of Dijkstra's shortest path algorithm. dist is a
    dictionary of minimum distances from some starting point to each key. col
    allows one to find the shortest path from a specific start point to a
    column. If set to False (the default), two specific points are expected.
    Also dist will not be returned unless col is set to True '''
    if not dist:
        for v in graph.keys():
            dist[v] = float("inf")
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        alt, v1 = min(queue)
        queue.remove((alt, v1))
        if col and v1[1] == end:
            return alt, dist
        elif v1 == end:
            return alt
        for v2 in graph[v1]:
            alt = dist[v1] + graph[v1][v2]
            if alt < dist[v2]:
                dist[v2] = alt
                queue.append((alt, v2))
    if col:
        return None, dist
    return None

# https://en.wikipedia.org/wiki/Farey_sequence#Next_term
def farey(n):
    ''' Generates the Farey sequence in ascending order. Can be used to
    generate pairs of coprime numbers '''
    a, b, c, d = 0, 1, 1, n
    yield a, b
    while c <= n:
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        yield a, b

def partition(parts, whole):
    ''' Calculate the number of ways 'whole' can be partitioned using 'parts' '''
    table = [0 for x in range(whole+1)]
    table[0] = 1
    for part in parts:
        for p in range(part, whole+1):
            table[p] += table[p - part]
    return table[whole]

def convergent(n, max_count):
    ''' Generator for convergents of 'n' '''
    period = periodic(n)
    length = len(period)
    num = [int(n**0.5), int(n**0.5), 1]
    denom = [1, 1, 0]
    index, count = 0, 0
    while max_count > count:
        num[0] = period[index]*num[1] + num[2]
        denom[0] = period[index]*denom[1] + denom[2]
        num[2], num[1] = num[1], num[0]
        denom[2], denom[1] = denom[1], denom[0]
        index = (index + 1) % length
        count += 1
        yield num[0], denom[0]

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def periodic(n):
    ''' Find period of continued fraction for sqrt(n). If n is a perfect square
    it returns an empty list '''
    m_cur, d_cur, a_cur = 0, 1, int(n**0.5)
    m_next, d_next, a_next = 0, 0, 0
    a0 = a_cur
    period = []
    if a_cur**2 == n:
        return period
    while a_cur != 2*a0:
        m_next = d_cur*a_cur - m_cur
        d_next = (n - m_next**2) // d_cur
        a_next = (a0 + m_next) // d_next
        m_cur, d_cur, a_cur = m_next, d_next, a_next
        period.append(a_next)
    return period

def sum_tri(tri):
    ''' For each pair of values in the last row of tri, add the greater value
    to the corresponding number in the row above. When all pairs are checked,
    delete the last row and return tri '''
    new_row = []
    for n in range(len(tri[-1]) - 1):
        new_row.append(max(tri[-1][n:n+2]) + tri[-2][n])
    tri[-2] = new_row
    del tri[-1]
    return tri

# https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_length(f_name):
    ''' Return line count of file '''
    line = []
    with open(f_name) as f:
        for line in enumerate(f):
            pass
    return line[0] + 1

def fib():
    ''' Generator of Fibonacci sequence terms '''
    pp, p = 1, 1
    while True:
        yield pp
        pp, p = p, p + pp

def gen_triple(limit=None):
    ''' Generator for primitive Pythagorean triples '''
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)