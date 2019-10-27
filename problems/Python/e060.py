''' Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime. '''

from collections import defaultdict
from primesieve.numpy import primes as primes_to

def main():
    ''' Driver function '''
    check = primes_to(10000**2)
    primes = check[check < 10000]
    graph = build_graph(primes, set(check))
    result = find_clique(graph)
    if result:
        print(sum(result))

def build_graph(primes, check):
    ''' Make a graph where vertices are primes and edges connect vertices that
    produce primes when concatenated in either order '''
    graph = defaultdict(set)
    for i, n1 in enumerate(primes):
        s1 = str(n1)
        for n2 in primes[i:]:
            s2 = str(n2)
            if int(s1+s2) in check and int(s2+s1) in check:
                graph[n1].add(n2)
                graph[n2].add(n1)
    return graph

def find_clique(graph):
    ''' Check all nodes in graph to determine if they are members of a clique
    of size 5. Edges refers to the nodes connected to node '''
    for node, edges in graph.items():
        result = find_set(graph, edges, {node})
        if result:
            return result
    return None

def find_set(graph, cur_set, final_set):
    ''' Determine if the cur_set contains a clique of size 5 '''
    for p in cur_set:
        new_set = cur_set.intersection(graph[p])
        final_set.add(p)
        if len(final_set) == 5:
            return final_set
        return find_set(graph, new_set, final_set)
    return None

if __name__ == "__main__":
    main()
