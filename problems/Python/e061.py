''' Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal,
and octagonal, is represented by a different number in the set. '''

from collections import defaultdict

def main():
    ''' Driver function '''
    polygons = [[n*(n+1)//2 for n in range(45, 141)],
                [n**2 for n in range(32, 100)],
                [n*(3*n-1)//2 for n in range(26, 82)],
                [n*(2*n-1) for n in range(23, 71)],
                [n*(5*n-3)//2 for n in range(21, 64)],
                [n*(3*n-2) for n in range(19, 59)]]
    graph = build_graph(polygons)
    loop = find_loop(graph)
    print(sum([n[0] for n in loop]))

def build_graph(polygons):
    ''' Make a graph where vertices are polygonal numbers and edges connect
    vertices with overlapping first/last digits. Edges point from last digits
    to first digits '''
    graph = defaultdict(set)
    for t1, l1 in enumerate(polygons[:-1]):
        for n1 in l1:
            for t2, l2 in enumerate(polygons[t1+1:]):
                t2 += t1 + 1
                for n2 in l2:
                    if n1%100 == n2//100:
                        graph[(n1, t1)].add((n2, t2))
                    if n2%100 == n1//100:
                        graph[(n2, t2)].add((n1, t1))
    return graph

def find_loop(graph):
    ''' Check all nodes in graph to determine if they are members of a loop of
    size 6, where each vertex in the loop is of a different polygonal type '''
    for node in graph:
        result = check_loop(graph, node, [node])
        if result:
            return result
    return None

def check_loop(graph, node, loop):
    ''' Determine if node is part of a loop of size 6 '''
    if len(loop) == 6:
        if loop[0] in graph[node]:
            return loop
        return None
    type_set = {n[1] for n in loop}
    for n in graph[node]:
        if n[1] not in type_set and n in graph:
            result = check_loop(graph, n, loop+[n])
            if result:
                return result
    return None

if __name__ == "__main__":
    main()
