''' Find the minimal path sum of the matrix in the source file from the
left column to the right column by moving right, up, and down '''

from euler import src, dijkstra, build_graph

def main():
    ''' Driver function '''
    graph, matrix = build_graph(src+'e081', True)
    min_dist = float("inf")
    dist = dict()
    for x in range(80):
        total, dist = dijkstra(graph, (x, 0), 79, dist, True)
        if not total:
            continue
        total += int(matrix[x][0])
        if total < min_dist:
            min_dist = total
    print(min_dist)

if __name__ == "__main__":
    main()
