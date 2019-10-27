''' Find the maximum total from top to bottom of the triangle found in the
source file '''

from euler import src, file_length, sum_tri

def main():
    ''' Apply sum_tri to triangle until only one row remains '''
    with open(src+'e067', 'r') as infile:
        triangle = [list(map(int, line.split())) for line in infile]
    for _ in range(file_length('e067') - 1):
        triangle = sum_tri(triangle)
    print(triangle[0][0])

if __name__ == "__main__":
    main()
