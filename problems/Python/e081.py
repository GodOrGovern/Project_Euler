''' Find the minimal path sum of the matrix in the source file from the top
left to the bottom right by only moving right and down '''

from euler import src, dijkstra, build_graph

def main():
    ''' Driver function '''
    graph, matrix = build_graph(src+'e081')
    total = dijkstra(graph, (0, 0), (79, 79))
    total += int(matrix[0][0])
    print(total)

if __name__ == "__main__":
    main()
