''' Find the smallest member of the longest amicable chain with no element
exceeding one million '''

from pyprimesieve import factorize

def main():
    ''' Driver function '''
    graph = build_graph(10**6)
    print(min(cycle_search(graph)))

def cycle_search(graph):
    ''' Find the longest cycle in 'graph'. Return as a set '''
    nodes = {n for n in graph.keys()}
    longest = set()
    visited = set()
    while nodes:
        temp = set()
        first = cur = nodes.pop()
        while cur in graph:
            if cur in visited:
                visited.update(temp)
                break
            temp.add(cur)
            if graph[cur] == first:
                if len(temp) > len(longest):
                    longest = temp
                break
            if graph[cur] in temp:
                break
            cur = graph[cur]
        if cur not in graph:
            visited.update(temp)
    return longest

def build_graph(end):
    ''' Build graph of amicable chains for all values up to 'end' '''
    graph = dict()
    for n in range(1, end):
        proper_sum = div_sum(n) - n
        if proper_sum < end:
            graph[n] = proper_sum
    return graph

def div_sum(n):
    ''' Return sum of divisors of 'n' '''
    total = 1
    for p, e in factorize(n):
        total *= (p**(e+1) - 1) // (p - 1)
    return total

if __name__ == "__main__":
    main()
